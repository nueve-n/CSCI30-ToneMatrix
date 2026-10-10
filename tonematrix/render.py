"""Render a pattern to a .wav file you can play in anything.

    python -m tonematrix.render patterns/pulse.txt out.wav --seconds 8

This is the "output device" for the project: it just calls next_sample()
over and over and writes the results to disk. Provided, do not modify.
"""

import argparse
import sys

from tonematrix.audio import SAMPLE_RATE, SAMPLES_PER_COLUMN, write_wav
from tonematrix.optimized import ToneMatrix
from tonematrix.songs import PRESETS, make_sequencer, preset_grid_size


def render(matrix, seconds, sample_rate=SAMPLE_RATE):
    """Collect `seconds` worth of samples from a matrix."""
    return [matrix.next_sample() for _ in range(int(seconds * sample_rate))]


def main(argv=None):
    parser = argparse.ArgumentParser(description="Render a tone matrix pattern to WAV.")
    parser.add_argument("pattern", nargs="?",
                        help="text file of '#' and '.', one line per row")
    parser.add_argument("output", nargs="?")
    parser.add_argument("--preset", choices=sorted(PRESETS),
                        help="coded preset from tonematrix/songs.py")
    parser.add_argument("--output", dest="output_option")
    parser.add_argument("--seconds", type=float)
    args = parser.parse_args(argv)

    output = args.output_option or args.output or "tonematrix.wav"
    if args.preset:
        if args.pattern and not args.output and not args.output_option:
            output = args.pattern
        try:
            matrix = ToneMatrix(preset_grid_size(args.preset))
            matrix.set_sequencer(make_sequencer(args.preset))
        except ValueError as exc:
            parser.error(str(exc))
        seconds = args.seconds
        if seconds is None:
            seconds = matrix.sequencer.loop_columns * SAMPLES_PER_COLUMN / SAMPLE_RATE
    else:
        if args.pattern is None:
            parser.error("a pattern file is required unless --preset is used")
        with open(args.pattern) as src:
            matrix = ToneMatrix.from_text(src.read())
        seconds = args.seconds if args.seconds is not None else 8.0

    print(f"{matrix.grid_size}x{matrix.grid_size} matrix, {seconds}s:")
    print(matrix.to_text())

    write_wav(output, render(matrix, seconds))
    print(f"wrote {output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
