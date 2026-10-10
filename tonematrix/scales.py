"""Which pitch belongs to which row. Provided, do not modify.

Row 0 is the *top* row of the matrix and has the highest pitch; row
grid_size-1 is the bottom row and has the lowest pitch. Pitches walk up
a C major scale, which is why almost any pattern you draw sounds vaguely
pleasant: every row belongs to the same key.
"""

# Semitone offsets of the C major scale, relative to the root.
_MAJOR = (0, 2, 4, 5, 7, 9, 11)
_NOTE_NAMES = ("C", "D", "E", "F", "G", "A", "B")

# Frequency of the lowest note we use (C2).
_ROOT_OCTAVE = 2
_ROOT_HZ = 65.406

# How many octaves the scale spans before it wraps back to the bottom. A
# 16-row matrix uses 16 scale degrees, so the wrap only shows up on unusually
# tall grids, where it keeps every string inside the audible range.
_OCTAVES = 4


def frequency_for_row(row, grid_size):
    """Return the frequency in hertz of the string on the given row.

    Rows are numbered from the top, so we flip the index before walking up
    the scale.
    """
    if not 0 <= row < grid_size:
        raise ValueError(f"row {row} out of range for a {grid_size}-row matrix")

    step = grid_size - 1 - row                     # 0 at the bottom row
    octave = (step // len(_MAJOR)) % _OCTAVES  # wrap so huge grids stay audible
    semitones = 12 * octave + _MAJOR[step % len(_MAJOR)]
    return _ROOT_HZ * 2.0 ** (semitones / 12.0)


def note_name_for_row(row, grid_size):
    """Return the C-major note name assigned to a row, such as C4 or G5."""
    if not 0 <= row < grid_size:
        raise ValueError(f"row {row} out of range for a {grid_size}-row matrix")

    step = grid_size - 1 - row
    octave = _ROOT_OCTAVE + (step // len(_MAJOR)) % _OCTAVES
    return f"{_NOTE_NAMES[step % len(_NOTE_NAMES)]}{octave}"


def scale_step_for_note_name(note):
    """Return the C-major scale step for a note name like C4, G4, or C5."""
    note = note.strip().upper()
    if len(note) < 2 or note[0] not in _NOTE_NAMES:
        raise ValueError(f"{note!r} is not a C-major note name like C4")

    try:
        octave = int(note[1:])
    except ValueError as exc:
        raise ValueError(f"{note!r} is not a C-major note name like C4") from exc

    scale_step = _NOTE_NAMES.index(note[0]) + (octave - _ROOT_OCTAVE) * len(_NOTE_NAMES)
    if scale_step < 0:
        raise ValueError(f"{note!r} is below the C{_ROOT_OCTAVE} matrix range")
    return scale_step


def row_for_note_name(note, grid_size):
    """Return the row that plays a C-major note name like C4, G4, or C5."""
    scale_step = scale_step_for_note_name(note)
    row = grid_size - 1 - scale_step
    if not 0 <= row < grid_size:
        raise ValueError(f"{note!r} is outside the {grid_size}-row matrix range")
    return row
