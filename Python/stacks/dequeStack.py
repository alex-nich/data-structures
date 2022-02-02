from collections import deque

"""
This script reviews stacks from Python's [collections.deque] module.
Stacks are linear data structures that employ LIFO ordering - last in, first out.

Operations to review include:
    Create - creating an empty stack
    Read - popping last element from stack
    Update - adding to top/end of stack
    Delete - removing a specific element from the stack
        (^^ does really apply here, although it can be done)
"""

#C = create empty stack
stack = deque()

#U = added elements to the stack
for i in range(10, 0, -1):
    stack.append(i)
    print("State of stack after insert: {}".format(stack))

#R = remove last element from stack
i = 1
maximum = len(stack)
print('\n')

while i < maximum:
    stack.pop()
    print("State of stack after read: {}".format(stack))
    i += 1

#D = delete 
print('\n')
stack.clear()
print("State of stack after clear: {}".format(stack))

#re add elements to stack
for i in range(10, 0, -1):
    stack.append(i)

#delete all even elements to stack
print('\n')
for i in range(2,10,2):
    stack.remove(i)
print("State of stack after deletion: {}".format(stack))