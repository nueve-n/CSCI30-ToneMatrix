from tonematrix.audio import SAMPLE_RATE
from tonematrix.ring_buffer import RingBuffer

# Height of the square wave written into the buffer by pluck().
PLUCK_AMPLITUDE = 0.05

# How much of its energy the string keeps on each trip around the buffer.
DECAY = 0.995


class StringInstrument:
    def __init__(self, frequency, sample_rate=SAMPLE_RATE):
        
        if frequency <= 0:
            raise ValueError("Frequency must be positive.")

        capacity = int(sample_rate // frequency)

        if capacity < 2:
            raise ValueError("Buffer capacity must be at least 2 samples.")

        self.frequency = frequency
        self.buffer = RingBuffer(capacity)

        for _ in range(capacity):
            self.buffer.enqueue(0.0)

    @classmethod
    def make_from_array(cls, values, frequency=None, sample_rate=SAMPLE_RATE):
        
        string = cls.__new__(cls)
        string.frequency = (frequency if frequency is not None
                            else sample_rate / len(values))
        string.buffer = RingBuffer(len(values))
        for value in values:
            string.buffer.enqueue(value)
        return string

    def __len__(self):
        
        return self.buffer.size()

    def pluck(self):
        
        capacity = self.buffer.capacity()
        halfway = capacity // 2

        while not self.buffer.is_empty():
            self.buffer.dequeue()

        for i in range(capacity):
            if i < halfway:
                self.buffer.enqueue(PLUCK_AMPLITUDE)
            else:
                self.buffer.enqueue(-PLUCK_AMPLITUDE)

    def next_sample(self):
        
        first = self.buffer.dequeue()
        second = self.buffer.peek()

        new_sample = DECAY * 0.5 * (first + second)
        self.buffer.enqueue(new_sample)

        return first

    def energy(self):
        
        total = 0.0
        n = self.buffer.size()
        for _ in range(n):
            value = self.buffer.dequeue()
            total += abs(value)
            self.buffer.enqueue(value)
        return total / n
