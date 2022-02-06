'''
Heaps are my favorite data structure :) they operate like a tree, but can be stored as an array!
----

Heaps are specialized tree-based data structures. 

Heaps are complete binary trees - a binary tree in which all the levels are 
    completely filled except possibly the lowest one, which is filled from the left

Heaps can come in one of two forms: 
    (1) MIN heap = the key present at the root node must be the minimum among 
    the keys of all its children. this relationship is recursively true for all sub-trees
    (2) MAX heap = the key present at the root node must be the maximum among 
    the keys of all its children. this relationship is recursively true for all sub-trees

When inserting or removing new nodes to the three, the heap properties must remain satisified. If
a insertion or deletion violates the heap properties, we must either heapify up (insertion) or
heapify down (deletion)

Nodes are inserted into the heap in level order.

When stored as an array, the following details the relationship between each node:
    - array[0] == root node
    - when i > 0:
        * parent node --> array[index] where index = (i-1)/2 
        * left child node --> array[index] where index = 2i + 1
        * right child node --> array[index] where index = 2i + 2
'''

### ----------------------------------- BEGIN heap
class Heap:
    def __init__(self):
        self.array = []

    def parentValue(self, i):
        ''' return value of parent node '''
        index = (i-1)//2 #must be integer division 
        return self.array[index]

    def parentIndex(self, i):
        ''' return index of parent node '''
        index = (i-1)//2 
        return index

    def hasParent(self, i):
        ''' return True if node has a parent node, False otherwise '''
        #only node that doesn't have a parent is the root node
        if self.parentIndex(i) < 0:
            return False
        return True

    def leftChildValue(self, i):
        ''' return value of left child node '''
        index = (2*i) + 1  
        return self.array[index]

    def leftChildIndex(self, i):
        ''' return index of left child node '''
        index = (2*i) + 1   
        return index

    def hasLeftChild(self, i):
        ''' return True if node has a left child node, False otherwise '''
        #to have a left child, the child's index must be less than the length of the array
        length = len(self.array)
        if self.leftChildIndex(i) >= length:
            return False
        return True

    def rightChildValue(self, i):
        ''' return value of right child node '''
        index = (2*i) + 2
        return self.array[index]

    def rightChildIndex(self, i):
        ''' return index of right child node '''
        index = (2*i) + 2  
        return index

    def hasRightChild(self, i):
        ''' return True if node has a right child node, False otherwise '''
        #to have a right child, the child's index must be less than the length of the array
        length = len(self.array)
        if self.rightChildIndex(i) >= length:
            return False
        return True

    def peekTop(self):
        ''' returns value of root node '''
        length = len(self.array)
        if length > 0:
            return self.array[0]

    def swap(self, parentIndex, childIndex):
        ''' swaps the value of two nodes '''
        
        #store value of parent noe
        parentValue = self.array[parentIndex]

        #set parent node to child node's value
        self.array[parentIndex] = self.array[childIndex]

        #set child node to parent node's value
        self.array[childIndex] = parentValue

    def print(self):
        ''' print heap in level order '''

        length = len(self.array)
        for i in range(length):
            if (i == 0 and length == 1) or (i == length - 1):
                print("{}".format(self.array[i]))
            else:
                print("{} -> ".format(self.array[i]), end="")
### ----------------------------------- END heap

### ----------------------------------- BEGIN min heap              
class MinHeap(Heap):

    def heapifyUp(self):
        
        #store index of last added node
        index = len(self.array) - 1

        #if parent exists and parent node is greater than value, continue loop
        while self.hasParent(index) and self.parentValue(index) > self.array[index]:

            #swap values of parent and child node
            parentIndex = self.parentIndex(index)
            self.swap(parentIndex, index)

            #set index to parent's index
            index = parentIndex


    def heapifyDown(self):

        #store index of root node
        index = 0

        #if node has children
        while self.hasLeftChild(index):
            left = self.leftChildValue(index)
            
            #only swap with right child if i'm greater than right AND right is lesser of the children
            if self.hasRightChild(index):
                right = self.rightChildValue(index)         

                if self.array[index] > right and right < left:
                    rightIndex = self.rightChildIndex(index)
                    self.swap(index, rightIndex)
                    #move to right child
                    index = rightIndex
                
            #only swap with left child if i'm greater than left AND left is lesser of the children
            if self.array[index] > left and left < right:
                leftIndex = self.leftChildIndex(index)
                self.swap(index, leftIndex)
                #move to left child
                index = leftIndex
            
            else:
                #node are in order. exit while loop
                break


    def add(self,value):
        #insert new node at the end
        self.array.append(value)

        #re apply heap properities
        self.heapifyUp()

    def delete(self):
        ''' removes and returns value of root node '''
        length = len(self.array)

        #if single element exist in heap, remove and return
        if length == 1:
                return self.array.pop()

        if length > 0:

            #store root value
            root = self.array[0]

            #replace root with right-most leaf node and remove right-most leaf node 
            self.array[0] = self.array.pop()

            #re apply heap properities
            self.heapifyDown()

            #return previous root
            return root
### ----------------------------------- END min heap
     
### ----------------------------------- BEGIN max heap
class MaxHeap(MinHeap):
    def heapifyUp(self):
        
        #store index of last added node
        index = len(self.array) - 1

        #if parent exists and parent node is less than value, continue loop
        while self.hasParent(index) and self.parentValue(index) < self.array[index]:

            #swap values of parent and child node
            parentIndex = self.parentIndex(index)
            self.swap(parentIndex, index)

            #set index to parent's index
            index = parentIndex


    def heapifyDown(self):

        #store index of root node
        index = 0

        #if node has children
        while self.hasLeftChild(index):
            left = self.leftChildValue(index)
            
            #only swap with right child if i'm lesser than right AND right is grester of the children
            if self.hasRightChild(index):
                right = self.rightChildValue(index)         

                if self.array[index] < right and right > left:
                    rightIndex = self.rightChildIndex(index)
                    self.swap(index, rightIndex)
                    #move to right child
                    index = rightIndex
                
            #only swap with left child if i'm lesser than left AND left is greater of the children
            if self.array[index] < left and left > right:
                leftIndex = self.leftChildIndex(index)
                self.swap(index, leftIndex)
                #move to left child
                index = leftIndex
            
            else:
                #node are in order. exit while loop
                break
### ----------------------------------- END max heap

def main():
    
    #input = [10, 30, 60, 40, 50, 90, 80, 20, 70, 100]
    input = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
    length = len(input)
    
    print("# ---------------------------- TOYING WITH MIN HEAP ---------------------------- #")
    #create empty min head
    minHeap = MinHeap()

    #add elements to heap
    for i in range(length):
        print("inserting {}: ".format(input[i]), end="")
        minHeap.add(input[i]) 
        minHeap.print()

    #peek at the min
    print("\nMin value in heap: {}".format(minHeap.peekTop()))

    #remove the min
    print("\nRemoving min [{}] value in heap: ".format(minHeap.delete()), end="")
    minHeap.print()

    #print nodes in ascending order
    print("\nMin Heap in ascending order: ", end="")
    for i in range(len(minHeap.array)):
        if len(minHeap.array) == 1:
            print("{}".format(minHeap.delete()))
        else:
            print("{} -> ".format(minHeap.delete()), end="")


    print("# ---------------------------- TOYING WITH MAX HEAP ---------------------------- #")
    #create empty min head
    maxHeap = MaxHeap()

    input = [10, 30, 60, 40, 50, 90, 80, 20, 70, 100]
    #input = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    #add elements to heap
    for i in range(length):
        print("inserting {}: ".format(input[i]), end="")
        maxHeap.add(input[i]) 
        maxHeap.print()

    #peek at the max
    print("\nMin value in heap: {}".format(maxHeap.peekTop()))

    #remove the max
    print("\nRemoving max [{}] value in heap: ".format(maxHeap.delete()), end="")
    maxHeap.print()

    #print nodes in descending order
    print("\nMax Heap in descending order: ", end="")
    for i in range(len(maxHeap.array)):
        if len(maxHeap.array) == 1:
            print("{}".format(maxHeap.delete()))
        else:
            print("{} -> ".format(maxHeap.delete()), end="")
        

if __name__ == "__main__":
    main()