import queue
from dequeQueue import DequeQueue

"""
This script implements a double ended queue by inheriting the functionality from
dequeQueue.py and adding new operations

"""

class DequeDoubleEndedQueue(DequeQueue):
    
    def append_front(self, element):
        self.queue.appendleft(element)

    def pop_end(self):
        return self.queue.pop()
