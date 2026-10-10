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
        self._sync_fast_buffer()

    @classmethod
    def make_from_array(cls, values, frequency=None, sample_rate=SAMPLE_RATE):
        
        string = cls.__new__(cls)
        string.frequency = (frequency if frequency is not None
                            else sample_rate / len(values))
        string.buffer = RingBuffer(len(values))
        for value in values:
            string.buffer.enqueue(value)
        string._sync_fast_buffer()
        return string

    def _sync_fast_buffer(self):
        self._data = self.buffer._data
        self._capacity = self.buffer.capacity()
        self._front = self.buffer._front

    def __len__(self):
        
        return self.buffer.size()

    def pluck(self):
        
        capacity = self._capacity
        halfway = capacity // 2

        data = self._data
        for i in range(capacity):
            if i < halfway:
                data[i] = PLUCK_AMPLITUDE
            else:
                data[i] = -PLUCK_AMPLITUDE
        self._front = 0
        self.buffer._front = 0
        self.buffer._rear = 0
        self.buffer._size = capacity

    def next_sample(self):
        
        data = self._data
        front = self._front
        capacity = self._capacity
        next_front = front + 1
        if next_front == capacity:
            next_front = 0

        first = data[front]
        second = data[next_front]

        new_sample = DECAY * 0.5 * (first + second)
        data[front] = new_sample
        self._front = next_front
        self.buffer._front = next_front
        self.buffer._rear = next_front

        return first

    def energy(self):
        
        total = 0.0
        data = self._data
        for value in data:
            total += abs(value)
        return total / self._capacity
