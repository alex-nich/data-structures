from random import randrange
import sys

"""
This script implements a singly linked list. 

Linked lists are linear data structures made of nodes. Each node is stored randommly throughout memory, 
however what links these node together are pointers. 

"""

class Node:
    ''' each node consists of two storage "compartments". 
    One stores the value of the node, 
    and the other stores the point to the next node'''
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

class SLinkedList:
    ''' each linked list can be identified by it's head node 
    (i.e., the first node in the list)'''

    #C = create "empty" linked list
    def __init__(self, head = None):
        self.head = head

    #U = added to end linked list
    def add_end(self, node):
        ''' adds a node to the beginning of the linked list'''
        current = self.head

        #find the last node in list
        while current.next is not None:
            current = current.next

        #set last's node next to new node
        current.next = node

    #U = added to beginning of linked list
    def add_beg(self, node):
        ''' adds a node to the beginning of the linked list'''
        #make the head of the list a new, seperate node
        next = self.head

        #set the head of the list to the new node
        self.head = node

        #make old head the second node of the lists
        self.head.next = next


    # R = print array
    def print(self):
        current = self.head

        #traverse list until at the end
        while current is not None:
            print(current.value, end=", ")
            current = current.next

    # R = return true if value exists in list
    def is_present(self, value):
        ''' returns true is value is present in list; false otherwise '''
        current = self.head

        #traverse list until at the end
        while current is not None:
            if current.value == value:
                return True
            else:
                current = current.next

        return False

    #D = remove a node from linked list
    def remove(self, value):
        ''' deletes elements from list, if they exists'''

        current = self.head
        previous = None

        #case 1: head is the node to remove
        if current.value == value:
            #make the next node the head node
            self.head = current.next
            current.next = None
            return 

        while current is not None:

            #if values are equal, node == found. break from loop
            if current.value == value:
                #break statements are used to execute code after for or while loop (i.e. exist loop)
                break

            #make the previous node the current node
            previous = current

            #make the next node the current node
            current = current.next

        #if current is None, value doesn't exists and can't be deleted
        if current is None:
            return

        #make the previous next pointer to the current's next (i.e. remove current)
        previous.next = current.next



def main():
    values = [int(arg) for arg in sys.argv[1:]]
    length = len(values)
    print("\nValues entered as input: {}".format(values))

    #use the first value to create a node
    node = Node(value = values[0])

    #make above node the head of the list
    llist = SLinkedList(node)

    print("\nValue of head node in linked list: {}".format(llist.head.value))

    #added rest of values to end of list
    for i in range(1,length):
        node = Node(value = values[i])
        llist.add_end(node)


    #print list
    print("\nPrinting Linked list: ", end = "")
    llist.print()

    #added new elements to beginning of list
    for i in range(2):
        node = Node(value = randrange(100))
        llist.add_beg(node)

        #print list
        print("\n\nPrinting Linked list after adding new node to beginning: ", end = "")
        llist.print()

    #searching for a value in linked list
    value = 666
    print("\n\nValue {} in list? {}".format(value, llist.is_present(value)))

    value = values[length//2]
    print("\nValue {} in list? {}".format(value, llist.is_present(value)))

    #removing first element from list
    value = node.value
    llist.remove(value)

    print("\nPrinting Linked list after removing first node ({}): ".format(value), end = "")
    llist.print()

    #removing inner element from list
    value = values[length//2]
    llist.remove(value)

    print("\n\nPrinting Linked list after removing inner node ({}): ".format(value), end = "")
    llist.print()

    #removing inner element from list
    value = 666
    llist.remove(value)

    print("\n\nPrinting Linked list after trying to remove a node that doesn't exists ({}): ".format(value), end = "")
    llist.print()


if __name__ == "__main__":
    main()

    #to run: 
    #python3 slinkedList.py 4 3 22 44 213 1 39 6 242