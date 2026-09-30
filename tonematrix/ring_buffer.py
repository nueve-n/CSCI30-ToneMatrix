from array import array


class RingBuffer:
    def __init__(self, capacity):
        if capacity < 1: raise ValueError("RingBuffer.__init__")

        self._data = array("d", [0.0] * capacity)
        self._front = 0
        self._rear = 0
        self._size = 0 

        # TODO (Milestone 2)

    def capacity(self) -> int:

        return len(self._data)

    def size(self) -> int:
               
        return self._size

    def is_empty(self) -> bool:

        return self._size == 0 

    def is_full(self) -> bool:

        return self.size() == self.capacity()

    def enqueue(self, x):
        
        if self.is_full(): raise IndexError("Ringbuffer.enqueue") 
        self._data[self._rear] = x

        if (self.capacity() - 1) == self._rear: self._rear = 0
        else: self._rear += 1

        self._size += 1

    def dequeue(self):

        if self.size() == 0: raise IndexError("RingBuffer.dequeue")

        num = self._data[self._front]
        self._data[self._front] = 0

        if (self.capacity() - 1) == self._front: self._front = 0
        else: self._front += 1

        self._size -= 1

        return num

    def peek(self) -> float: #check just in case length error
        
        if self.is_empty(): raise IndexError("RingBuffer.peek")
        return self._data[self._front]
        

    def __len__(self):
        
        return self.size()
