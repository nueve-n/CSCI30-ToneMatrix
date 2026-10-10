"""Code-driven song presets for the tone matrix.

Edit PRESETS to make the app play a song without manually clicking cells.
Each item is one swept column/beat. Put one note, several notes, or a rest.
"""

from tonematrix.scales import row_for_note_name, scale_step_for_note_name

REST = []


PRESETS = {
    "Twinkle": [
        ["C4 C5 G4"],
        ["C4"], ["C4"], ["G4"], ["G4"],
        ["A4"], ["A4"], ["G4"], [],
        ["F4"], ["F4"], ["E4"], ["E4"],
        ["D4"], ["D4"], ["C4"], [],
        ["G4"], ["G4"], ["F4"], ["F4"],
        ["E4"], ["E4"], ["D4"], [],
        ["G4"], ["G4"], ["F4"], ["F4"],
        ["E4"], ["E4"], ["D4"], [],
        ["C4"], ["C4"], ["G4"], ["G4"],
        ["A4"], ["A4"], ["G4"], [],
        ["F4"], ["F4"], ["E4"], ["E4"],
        ["D4"], ["D4"], ["C4"], [],
    ],
    "Chord Loop": [
        "C4 E4 G4", REST, "F4 A4 C5", REST,
        "G4 B4 D5", REST, "C4 E4 C5", REST,
    ],
    "Stereo Madness": [
        # Measure 1
        "C5",
        "G5",
        "C5",
        "G5",
        "C5",
        "G5",
        "C5",
        "G5",
        # Measure 2
        "G4",
        "D5",
        "G4",
        "D5",
        "G4",
        "D5",
        "G4",
        "D5",
        # Measure 3
        "A4",
        "E5",
        "A4",
        "E5",
        "A4",
        "E5",
        "A4",
        "E5",
        # Measure 4
        "F4",
        "C5",
        "F4",
        "C5",
        "F4",
        "C5",
        "F4",
        "C5",
        # Measure 5
        "C5",
        "G5",
        "C5",
        "G5",
        "C5",
        "G5",
        "C5",
        "G5",
        # Measure 6
        "G4",
        "D5",
        "G4",
        "D5",
        "G4",
        "D5",
        "G4",
        "D5",
        # Measure 7
        "A4",
        "E5",
        "A4",
        "E5",
        "A4",
        "E5",
        "A4",
        "E5",
        # Measure 8
        "F4",
        "C5",
        "F4",
        "C5",
        "F4",
        "C5",
        "F4",
        "C5",
        # Measure 9
        "C4  C5",
        "G4  G5",
        "C4  C5",
        "G4  G5",
        "C4  C5",
        "G4  G5",
        "C4  C5",
        "G4  G5",
        # Measure 10
        "G3  G4",
        "D4  D5",
        "G3  G4",
        "D4  D5",
        "G3  G4",
        "D4  D5",
        "G3  G4",
        "D4  D5",
        # Measure 11
        "A3  A4",
        "E4  E5",
        "A3  A4",
        "E4  E5",
        "A3  A4",
        "E4  E5",
        "A3  A4",
        "E4  E5",
        # Measure 12
        "F3  F4",
        "C4  C5",
        "F3  F4",
        "C4  C5",
        "F3  F4",
        "C4  C5",
        "F3  F4",
        "C4  C5",
        # Measure 13
        "C4  C5",
        "G4  G5",
        "C4  C5",
        "G4  G5",
        "C4  C5",
        "G4  G5",
        "C4  C5",
        "G4  G5",
        # Measure 14
        "G3  G4",
        "D4  D5",
        "G3  G4",
        "D4  D5",
        "G3  G4",
        "D4  D5",
        "G3  G4",
        "D4  D5",
        # Measure 15
        "A3  A4",
        "E4  E5",
        "A3  A4",
        "E4  E5",
        "A3  A4",
        "E4  E5",
        "A3  A4",
        "E4  E5",
        # Measure 16
        "F3  F4",
        "C4  C5",
        "F3  F4",
        "C4  C5",
        "F3  F4",
        "C4  C5",
        "F3  F4",
        "C4  C5",
        # Measure 17 (whole note, tied from m16)
        "C4  C5",
        # Measure 18
        "C4  C5",
        "G4  G5",
        "C4  C5",
        "G4  G5",
        "C4  C5",
        "G4  G5",
        "C4  C5",
        "G4  G5",
        # Measure 19
        "G3  G4",
        "D4  D5",
        "G3  G4",
        "D4  D5",
        "G3  G4",
        "D4  D5",
        "G3  G4",
        "D4  D5",
        # Measure 20
        "A3  A4",
        "E4  E5",
        "A3  A4",
        "E4  E5",
        "A3  A4",
        "E4  E5",
        "A3  A4",
        "E4  E5",
        # Measure 21
        "F3  F4",
        "C4  C5",
        "F3  F4",
        "C4  C5",
        "F3  F4",
        "C4  C5",
        "F3  F4",
        "C4  C5",
        # Measure 22
        "C4  C5",
        "G4  G5",
        "C4  C5",
        "G4  G5",
        "C4  C5",
        "G4  G5",
        "C4  C5",
        "G4  G5",
        # Measure 23
        "G3  G4",
        "D4  D5",
        "G3  G4",
        "D4  D5",
        "G3  G4",
        "D4  D5",
        "G3  G4",
        "D4  D5",
        # Measure 24
        "A3  A4",
        "E4  E5",
        "A3  A4",
        "E4  E5",
        "A3  A4",
        "E4  E5",
        "A3  A4",
        "E4  E5",
        # Measure 25
        "F3  F4",
        "C4  C5",
        "F3  F4",
        "C4  C5",
        "F3  F4",
        "C4  C5",
        "F3  F4",
        "C4  C5",
        # Measure 26
        "C4  C5",
        "G4  G5",
        "C4  C5",
        "G4  G5",
        "C4  C5",
        "G4  G5",
        "C4  C5",
        "G4  G5",
        # Measure 27
        "G3  G4",
        "D4  D5",
        "G3  G4",
        "D4  D5",
        "G3  G4",
        "D4  D5",
        "G3  G4",
        "D4  D5",
        # Measure 28
        "A3  A4",
        "E4  E5",
        "A3  A4",
        "E4  E5",
        "A3  A4",
        "E4  E5",
        "A3  A4",
        "E4  E5",
        # Measure 29
        "F3  F4",
        "C4  C5",
        "F3  F4",
        "C4  C5",
        "F3  F4",
        "C4  C5",
        "F3  F4",
        "C4  C5",
        # Measure 30
        "C4  C5",
        "G4  G5",
        "C4  C5",
        "G4  G5",
        "C4  C5",
        "G4  G5",
        "C4  C5",
        "G4  G5",
        # Measure 31
        "G3  G4",
        "D4  D5",
        "G3  G4",
        "D4  D5",
        "G3  G4",
        "D4  D5",
        "G3  G4",
        "D4  D5",
        # Measure 32
        "A3  A4",
        "E4  E5",
        "A3  A4",
        "E4  E5",
        "A3  A4",
        "E4  E5",
        "A3  A4",
        "E4  E5",
        # Measure 33
        "F3  F4",
        "C4  C5",
        "F3  F4",
        "C4  C5",
        "F3  F4",
        "C4  C5",
        "F3  F4",
        "C4  C5",
        # Measure 34 (8vb, sounding pitch)
        "C4",
        "C5",
        "C4",
        "C5",
        "C4",
        "C5",
        "C4",
        "C5",
        # Measure 35 (8vb, sounding pitch)
        "G3",
        "G4",
        "G3",
        "G4",
        "G3",
        "G4",
        "G3",
        "G4",
        # Measure 36 (8vb, sounding pitch)
        "A3",
        "A4",
        "A3",
        "A4",
        "A3",
        "A4",
        "A3",
        "A4",
        # Measure 37 (8vb, sounding pitch)
        "F3",
        "F4",
        "F3",
        "F4",
        "F3",
        "F4",
        "F3",
        "F4",
        # Measure 38 (8vb, sounding pitch)
        "C4",
        "C5",
        "C4",
        "C5",
        "C4",
        "C5",
        "C4",
        "C5",
        # Measure 39 (8vb, sounding pitch)
        "G3",
        "G4",
        "G3",
        "G4",
        "G3",
        "G4",
        "G3",
        "G4",
        # Measure 40 (8vb, sounding pitch)
        "A3",
        "A4",
        "A3",
        "A4",
        "A3",
        "A4",
        "A3",
        "A4",
        # Measure 41 (8vb, sounding pitch)
        "F3",
        "F4",
        "F3",
        "F4",
        "F3",
        "F4",
        "F3",
        "F4",
        REST,
        REST,
        REST,
        REST,
        REST,
        REST,
        REST,
        REST,
        # Measure 50 (whole note chord, accented, 8vb)
        "C4  C5"
    ],
    "Stereo Madness 2": [
        REST,
        REST,
        REST,
        REST,
        REST,
        REST,
        REST,
        REST,
        REST,
        REST,
        REST,
        REST,
        REST,
        REST,
        REST,
        REST,
        REST,
        REST,
        # Measure 18
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        # Measure 19
        "C4  C5",
        "B3  B4",
        "B3  B4",
        "B3  B4",
        "B3  B4",
        "B3  B4",
        "B3  B4",
        "B3  B4",
        # Measure 20
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        # Measure 21
        "C4  C5",
        "D4  D5",
        "D4  D5",
        "D4  D5",
        "D4  D5",
        "D4  D5",
        "D4  D5",
        "D4  D5",
        # Measure 22
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        # Measure 23
        "C4  C5",
        "B3  B4",
        "B3  B4",
        "B3  B4",
        "B3  B4",
        "B3  B4",
        "B3  B4",
        "B3  B4",
        # Measure 24
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        # Measure 25
        "C4  C5",
        "D4  D5",
        "D4  D5",
        "D4  D5",
        "D4  D5",
        "D4  D5",
        "D4  D5",
        "E4  E5",
        # Measure 26
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        # Measure 27
        "C4  C5",
        "B3  B4",
        "B3  B4",
        "B3  B4",
        "B3  B4",
        "B3  B4",
        "B3  B4",
        "B3  B4",
        # Measure 28
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        # Measure 29
        "C4  C5",
        "D4  D5",
        "D4  D5",
        "D4  D5",
        "D4  D5",
        "D4  D5",
        "D4  D5",
        "D4  D5",
        # Measure 30
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        # Measure 31
        "C4  C5",
        "B3  B4",
        "B3  B4",
        "B3  B4",
        "B3  B4",
        "B3  B4",
        "B3  B4",
        "B3  B4",
        # Measure 32
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        # Measure 33
        "C4  C5",
        "D4  D5",
        "D4  D5",
        "D4  D5",
        "D4  D5",
        "D4  D5",
        "E4  E5",
        "E4  E5",
        # Measure 34
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        # Measure 35
        "C4  C5",
        "B3  B4",
        "B3  B4",
        "B3  B4",
        "B3  B4",
        "B3  B4",
        "B3  B4",
        "B3  B4",
        # Measure 36
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        # Measure 37
        "C4  C5",
        "D4  D5",
        "D4  D5",
        "D4  D5",
        "D4  D5",
        "D4  D5",
        "D4  D5",
        "D4  D5",
        # Measure 38
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        # Measure 39
        "C4  C5",
        "B3  B4",
        "B3  B4",
        "B3  B4",
        "B3  B4",
        "B3  B4",
        "B3  B4",
        "B3  B4",
        # Measure 40
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        "C4  C5",
        # Measure 41
        "C4  C5",
        "D4  D5",
        "D4  D5",
        REST,
        "E4  E5",
        "E4  E5",
        "E4  E5",
        REST,
        # Measure 42
        "C4  C5",
        "C4  C5",
        REST,
        "C4  C5",
        "C4  C5",
        REST,
        "C4  C5",
        "C4  C5",
        # Measure 43
        "C4  C5",
        "B3  B4",
        REST,
        "B3  B4",
        "B3  B4",
        REST,
        "B3  B4",
        "B3  B4",
        # Measure 44
        "C4  C5",
        "C4  C5",
        REST,
        "C4  C5",
        "C4  C5",
        REST,
        "C4  C5",
        "C4  C5",
        # Measure 45
        "C4  C5",
        "D4  D5",
        REST,
        "D4  D5",
        "D4  D5",
        REST,
        "D4  D5",
        "D4  D5",
        # Measure 46
        "C4  C5",
        "C4  C5",
        REST,
        "C4  C5",
        "C4  C5",
        REST,
        "C4  C5",
        "C4  C5",
        # Measure 47
        "C4  C5",
        "B3  B4",
        REST,
        "B3  B4",
        "B3  B4",
        REST,
        "B3  B4",
        "B3  B4",
        # Measure 48
        "C4  C5",
        "C4  C5",
        REST,
        "C4  C5",
        "C4  C5",
        REST,
        "C4  C5",
        "C4  C5",
        # Measure 49
        "C4  C5",
        "D4  D5",
        REST,
        "D4  D5",
        "E4  E5",
        REST,
        "E4  E5",
        "E4  E5",
        # Measure 50
        REST
    ]
}


def notes(*names):
    """Write one beat/chord: notes("C4", "E4", "G4")."""
    return names


def rest():
    """Write one silent beat."""
    return REST


def _normalize_step(step):
    if step is None:
        return ()
    if isinstance(step, str):
        return tuple(part for part in step.replace(",", " ").split() if part)

    names = []
    for part in step:
        names.extend(_normalize_step(part))
    return tuple(names)


def required_grid_size(steps, preset_name="preset"):
    """Smallest grid that can play every note in a preset."""
    highest_step = 0
    for index, step in enumerate(steps, start=1):
        for note in _normalize_step(step):
            try:
                highest_step = max(highest_step, scale_step_for_note_name(note))
            except ValueError as exc:
                measure = (index - 1) // 8 + 1
                beat = (index - 1) % 8 + 1
                message = (f"{preset_name!r} has bad note {note!r} at step {index} "
                           f"(measure {measure}, beat {beat})")
                raise ValueError(message) from exc
    return highest_step + 1


def preset_grid_size(name, minimum=16, choices=(4, 8, 12, 16, 24, 32)):
    """Return the smallest available grid size that can play a preset."""
    needed = max(minimum, required_grid_size(PRESETS[name], name))
    for size in choices:
        if size >= needed:
            return size
    return needed


class SongSequencer:
    """Feeds coded song steps into matrix columns as the playhead moves."""

    def __init__(self, steps):
        if not steps:
            raise ValueError("a song preset needs at least one step")
        self.steps = [_normalize_step(step) for step in steps]
        self.next_step = 0

    @property
    def loop_columns(self):
        return len(self.steps)

    def reset(self):
        self.next_step = 0

    def seed(self, matrix):
        """Fill the visible grid with the first screenful of song steps."""
        self.reset()
        for col in range(matrix.grid_size):
            self.write_next_column(matrix, col)

    def advance_after_sweep(self, matrix, col):
        """Replace a just-played column with the next coded song step."""
        self.write_next_column(matrix, col)

    def write_next_column(self, matrix, col):
        notes = self.steps[self.next_step % len(self.steps)]
        rows = {row_for_note_name(note, matrix.grid_size) for note in notes}
        for row in range(matrix.grid_size):
            matrix.set_cell(row, col, row in rows)
        self.next_step += 1


def make_sequencer(name):
    return SongSequencer(PRESETS[name])
