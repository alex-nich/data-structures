from collections import deque
from random import randint
import sys

"""
This script reviews queues from Python's [collection module].
Queue are linear data structures that employ FIFO ordering - first in, first out
"""

class DequeQueue:
    #C = create
    def __init__(self):
        ''' initialize an empty queue'''

        self.queue = deque()

    #R = read
    def pop(self):
        ''' remove first element from queue '''
        return self.queue.popleft()

    #U = update
    def append(self, element):
        ''' add an element to end of queue '''
        self.queue.append(element)

    #D = delete (not normal operation, but why not)
    def delete(self, element):
        ''' removes all occurences of an element in the queue '''
        while element in self.queue:
            self.queue.remove(element)

    #setters and getters
    def set_queue(self, q):
        self.queue = q

    def get_queue(self):
        return self.queue

def main():
    for arg in sys.argv[1:]:
        print(arg)

    #create a queue object
    q = DequeQueue()

    #add elements to queue
    for i in [x**2 for x in range(10)]:
        q.append(i)
        
        #print queue
        print("State of queue after insert: {}".format(q.get_queue()))

    #element wise acces
    res = q.get_queue()
    index = randint(0,9)
    print("\nElement wise access to element {}: {}".format(index, res[index]))

    #pop from queue
    element = q.pop()
    print("\nElement 0 popped from queue: {}".format(element))
    print("State of queue after pop: {}".format(q.get_queue()))

    #delete element from queue
    element = 25
    q.delete(element)
    print("\nElement to be deleted from queue: {}".format(element))
    print("State of queue deletion: {}".format(q.get_queue()))


if __name__ == "__main__":
    main()
