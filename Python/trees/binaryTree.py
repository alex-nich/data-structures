'''
Trees are non-linear data structures that store data in a hierarchical fashion.
Trees are similar to linked list in that they are constructed using node. 
Each node stores data and pointers to the left, right, and parent nodes (optional).
A pointer to the parent node can be useful if the traversal path needs to be recovered.

A binary tree is a special tree where any node can have at max two children. 

BT operations:
    - C = create an empty tree
    - R = traverse the tree (preorder, inorder, postorder) / search for value in tree (store path)
    - U = insert new node to tree 
    - D = delete a node from the tree
'''

import sys
from collections import deque
from typing import Deque
from unittest.mock import NonCallableMagicMock

from sklearn.linear_model import lars_path_gram

class Node:
    def __init__(self, value = None, left = None, right = None, parent = None):
        '''create an empty Node'''
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

class BinaryTree:
    def __init__(self, root = None):
        '''create an empty tree tree '''
        self.root = root

    def insert(self, node):
        '''insert new node to tree  '''
        #if root is None, first node is root of tree
        if self.root is None:
            self.root = node
        else:
            #use a queue to traverse the tree in level order and add new node in next avaliable spot
            queue = deque()
            queue.append(self.root)

            while len(queue) > 0:
                
                #pop the current node from queue
                current = queue.popleft()

                #if current node has no LEFT child, add new node
                if current.left is None:
                    node.parent = current
                    current.left = node
                    break #exist while loop
                else:
                    #if current node has a LEFT child, add LEFT child to queue
                    queue.append(current.left)

                #if current node has no RIGHT child, add new node
                if current.right is None:
                    node.parent = current
                    current.right = node
                    break #exist while loop
                else:
                    #if current node has a RIGHT child, add RIGHT child to queue
                    queue.append(current.right)
      
    def find_path(self, node):    
        ''' returns path to node '''
        #use stack to print in reverse order 
        stack = deque()

        #add node in question
        stack.append(node)

        #loop until parent is none (i.e. root of tree)
        parent = node.parent
        while parent is not None:
            stack.append(parent)
            parent = parent.parent

        return stack

    
    def print_path(self, path, reverse = True):
        ''' print path'''

        #if reverse is true, treat path like a stack
        if reverse:
            while path:
                node = path.pop()
                #if operating with root node, no need to follow with arrow
                if len(path) == 0:
                    print("{} ".format(node.value))
                else:
                    print("{} -> ".format(node.value), end="")
        else:
            length = len(path)
            for i in range(length):
                node = path[i]
                if i == length -1:
                    print("{} ".format(node.value))
                else:
                    print("{} -> ".format(node.value), end="")

        

    def search(self, value):
        '''return node if value exists, False otherwise'''

        #use a queue to traverse the tree in level order and check if node.value == value
        queue = deque()
        queue.append(self.root)

        while len(queue) > 0:
            
            #pop the current node from queue
            current = queue.pop()

            #check if current node.value == value
            if current.value == value:
                return (current)
            
            #if not, add children nodes (left, then right) to queue 
            else:
                if current.left is not None:
                    queue.append(current.left)

                if current.right is not None:
                    queue.append(current.right)

        #return False if value can't be found
        return False

    #------------ don't ya just love recurison :)
    def preorder(self, current): #, current = self.root):
        '''traverse the tree using pre-order ordering'''
        #Root -> Left -> Right

        #create empty path list
        path = []

        if current is not None:
            #add root node to list
            path.append(current)
            #traverse root's LEFT subtree and join path results
            path = path + self.preorder(current.left)
            #traverse root's RIGHT subtree and join path results
            path = path + self.preorder(current.right)
        
        return path

    def inorder(self, current):
        '''traverse the tree using in-order ordering '''
        #Left -> Root -> Right
        
        #create empty path list
        path = []

        if current is not None:
            #traverse root's LEFT subtree and join path results
            path = path + self.inorder(current.left)
            #add root node to list
            path.append(current)
            #traverse root's RIGHT subtree and join path results
            path = path + self.inorder(current.right)
        
        return path

    def postorder(self, current):
        '''traverse the tree using post-order ordering'''
        #Left -> Right -> Root
        #create empty path list
        path = []

        if current is not None:
            #traverse root's LEFT subtree and join path results
            path = path + self.postorder(current.left)
            #traverse root's RIGHT subtree and join path results
            path = path + self.postorder(current.right)
            #add root node to list
            path.append(current)
        
        return path
    #------------ end recursive functions

    def delete(self, value):
        '''delete a node from the tree'''
        
        #1. find node to delete
        to_delete = self.search(value)

        #2. find last (most right) leaf node
        current = self.root
        queue = deque()
        queue.append(current)

        while len(queue) > 0:
            current = queue.popleft()

            #add left and right nodes into the queue until the LAST node in queue has no children
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
            if current.left is None and current.left is None and len(queue) == 0:
                last = current


        #3. set node-to-be-deleted value to last leaf node's value
        to_delete.value = last.value

        #4. set last leaf node's parent's (left||right) pointer to None
        if last.parent.left == last:
            last.parent.left = None
        elif last.parent.right == last:
            last.parent.right = None

        #5. (finally) set last leaf node's pointers to None
        last.left = None
        last.right = None
        last.parent = None
        

def main():
    #tree is passed in a list
    #example: A B C D E F G H I J
    input = []
    for arg in sys.argv[1:]:
        input.append(arg)

    #construct tree from input
    bt = BinaryTree()
    total = len(input)
    for i in range(total):
        #create new node
        node = Node(value = input[i])
        bt.insert(node)


    #search for Node
    for value in ["M", "J", "10", "6"]:
        result = bt.search(value)
        
        if result:

            print("\nNode [{}] found in tree: ".format(result.value), end="")
            
            #find path to node
            path = bt.find_path(result)
            bt.print_path(path)
            
        else:
            print("\nDoes node [{}] exist in tree? {}".format(value, result))

    #pre order traversal
    path = bt.preorder(bt.root)
    print("\nPreorder traversal result: ", end="")
    bt.print_path(path, reverse=False)

    #post order traversal
    path = bt.postorder(bt.root)
    print("\nPostorder traversal result: ", end="")
    bt.print_path(path, reverse=False)

    #in order traversal
    path = bt.inorder(bt.root)
    print("\nInorder traversal result: ", end="")
    bt.print_path(path, reverse=False)

    #delete a node:
    value = "C" #trying to inner node
    #value = "A" #trying to delete root node
    #value = "F" #trying to delete another leaf node
    bt.delete(value)

    print("\nInorder traversal of tree after deleting node [{}]: ".format(value), end="")
    path = bt.inorder(bt.root)
    bt.print_path(path, reverse=False)

if __name__ == "__main__":
    main()