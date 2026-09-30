from tonematrix.audio import SAMPLE_RATE, SAMPLES_PER_COLUMN
from tonematrix.scales import frequency_for_row
from tonematrix.string_instrument import StringInstrument

ON = "#"
OFF = "."
SILENCE_THRESHOLD = 1e-5


class ToneMatrix:
    def __init__(self, grid_size, sample_rate=SAMPLE_RATE,
                 samples_per_column=SAMPLES_PER_COLUMN):
        if grid_size < 1:
            raise ValueError("grid_size must be at least 1.")
        
        self.grid_size = grid_size
        self.samples_per_column = samples_per_column
        self.sample_rate = sample_rate

        self.grid = [False] * (grid_size ** 2)
        self.instruments = [StringInstrument(frequency_for_row(row, grid_size),
                                             sample_rate=sample_rate)
                            for row in range(grid_size)]
        self.active_rows = []
        self.energy_check_index = 0

        self.column = 0
        self.drag_value = None  
        self.sample_count = 0  
        self.samples_until_column = 0
        
    def index_of(self, row, col):
        
        if not (0 <= row < self.grid_size) or not (0 <= col < self.grid_size):
            raise IndexError("Position out of bounds.") 

        return row * self.grid_size + col
    
    def is_on(self, row, col):

        return self.grid[self.index_of(row, col)]

    def set_cell(self, row, col, value):

        self.grid[self.index_of(row, col)] = bool(value)

    def press(self, row, col):

        self.set_cell(row, col, not self.is_on(row, col))
        self.drag_value = self.is_on(row, col)
 
    def drag(self, row, col):

        self.set_cell(row, col, self.drag_value)

    def clear(self):

        for i in range(len(self.grid)):
            self.grid[i] = False

        self.active_rows.clear()

    def next_sample(self):

        if self.samples_until_column == 0:
            self.retire_quiet_row()
            self.pluck_column(self.column)
            self.column = (self.column + 1) % self.grid_size
            self.samples_until_column = self.samples_per_column - 1
        else:
            self.samples_until_column -= 1

        self.sample_count += 1

        total = 0.0
        active_rows = self.active_rows
        instruments = self.instruments
        for row in active_rows:
            total += instruments[row].next_sample()

        return total

    def pluck_column(self, col):

        for row in range(self.grid_size):
            if self.is_on(row, col):
                self.instruments[row].pluck()
                if row not in self.active_rows:
                    self.active_rows.append(row)

    def retire_quiet_row(self):
        
        if not self.active_rows:
            self.energy_check_index = 0
            return

        index = self.energy_check_index % len(self.active_rows)
        row = self.active_rows[index]
        if self.instruments[row].energy() <= SILENCE_THRESHOLD:
            last_row = self.active_rows.pop()
            if index < len(self.active_rows):
                self.active_rows[index] = last_row
            self.energy_check_index %= max(1, len(self.active_rows))
        else:
            self.energy_check_index = (index + 1) % len(self.active_rows)

    def resize(self, new_size):

        if new_size < 1:
            raise ValueError("new_size must be at least 1.")

        old_size = self.grid_size
        new_grid = [False] * (new_size ** 2)

        min_size = min(old_size, new_size)
        for row in range(min_size):
            for col in range(min_size):
                new_grid[row * new_size + col] = self.is_on(row, col)   

        new_instruments = []
        for row in range(new_size):
            if row < old_size:
                new_instruments.append(self.instruments[row])
            else:
                new_instruments.append(StringInstrument(frequency_for_row(row, new_size),
                                                        sample_rate=self.sample_rate))

        self.grid_size = new_size
        self.grid = new_grid
        
        self.instruments = new_instruments
        self.active_rows = []
        for row, instrument in enumerate(self.instruments):
            if instrument.energy() > SILENCE_THRESHOLD:
                self.active_rows.append(row)
        self.energy_check_index = 0
        self.column = 0
        self.sample_count = 0
        self.samples_until_column = 0

    def to_text(self):
        lines = []
        for row in range(self.grid_size):
            line = ''.join(ON if self.is_on(row, col) else OFF
                           for col in range(self.grid_size))
            lines.append(line)
        
        return '\n'.join(lines)

    @classmethod
    def from_text(cls, text, **kwargs):
        rows = [line.strip() for line in text.strip().splitlines() if line.strip()]
        size = len(rows)
        if any(len(line) != size for line in rows):
            raise ValueError("pattern must be square")

        matrix = cls(size, **kwargs)
        for r, line in enumerate(rows):
            for c, ch in enumerate(line):
                matrix.set_cell(r, c, ch == ON)
        return matrix

    def __str__(self):
        return self.to_text()
