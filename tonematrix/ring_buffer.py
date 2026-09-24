"""Part 1: a fixed-capacity ring buffer.

A queue that never grows. It holds at most `capacity` floats; enqueueing into
a full buffer or dequeueing from an empty one is an error, not a resize.

Rules for this file:
  * The storage is `array("d", ...)` of exactly `capacity` elements,
    allocated once in __init__ and never replaced. Keep it in `self._data`.
  * No list, no dict, no collections.deque, no NumPy. This is checked.
  * Every operation must run in constant time. In particular, dequeue() must
    not shuffle the remaining items down by one.
"""

from array import array


class RingBuffer:
    """A circular queue of floats with a fixed capacity."""

    def __init__(self, capacity):
        """Create an empty buffer that can hold `capacity` items.

        Set up four things:
          * self._data  - array("d") of `capacity` zeros
          * self._front - index of the least recently enqueued item
          * self._rear  - index one past the most recently enqueued item
          * self._size  - how many items are in the buffer right now

        Raise ValueError if capacity is less than 1.
        """
        if capacity < 1: raise ValueError("RingBuffer.__init__")

        self._data = array("d", [0.0] * capacity)
        self._front = 0
        self._rear = 0
        self._size = 0 

        # TODO (Milestone 2)

    def capacity(self) -> int:
        """The most items this buffer can hold."""

        return len(self._data)
        # TODO (Milestone 2)

    def size(self) -> int:
        """How many items are in the buffer right now."""

        return self._size
        # TODO (Milestone 2)

    def is_empty(self) -> bool:

        return self._size == 0 
        # TODO (Milestone 2)

    def is_full(self) -> bool:

        return self.size() == self.capacity()
        # TODO (Milestone 2)

    def enqueue(self, x):
        """Add x at the rear. 
        
        Raise IndexError if the buffer is already full.
        """
        if self.is_full(): 
            raise IndexError("Ringbuffer.enqueue") 
        
        self._data[self._rear] = x
        self._rear += 1

        if self._rear == self.capacity():
            self._rear = 0
        
        self._size += 1

        # TODO (Milestone 3)

    def dequeue(self):
        """Remove and return the item at the front. 

        Raise IndexError if the buffer is empty.
        """

        if self.is_empty(): 
            raise IndexError("RingBuffer.dequeue")

        item = self._data[self._front]
        self._data[self._front] = 0.0
        self._front += 1

        if self._front == self.capacity():
            self._front = 0

        self._size -= 1
        return item
        # TODO (Milestone 3)

    def peek(self) -> float: #check just in case length error
        """Return the item at the front without removing it.

        Raise IndexError if the buffer is empty.
        """

        if self.is_empty():
            raise IndexError("RingBuffer.peek")
        return self._data[self._front]
        
        # TODO (Milestone 3)

    def __len__(self):
        """So that len(buffer) works. Provided, once size() works."""
        return self.size()
