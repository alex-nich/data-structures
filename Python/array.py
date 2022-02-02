import numpy as np
import sys

class DynamicArray:

    #C = create
    def __init__(self, sort_flg = False):
        ''' initialize object 
            * operation complexity: O(1)
        '''
        self.__darray = []
        self.__sort_flg = sort_flg

    #R = read (search)
    def search(self,element):
        ''' return index of element if exists in array. else return -1 
            * operation complexity: O(n)
        '''
        
        #element can't exist in empty list
        if len(self.__darray) == 0:
            return -1

        for i in range(len(self.__darray)):
            if self.__darray[i] == element:
                return i
        
        return -1

    #U = update (insert)
    def insert(self, element):
        ''' insert new element into array 
            * operation complexity (if sorted): O(n)
            * operation complexity (if not sorted): O(1) **
        '''

        length = len(self.__darray)
        
        if self.__sort_flg and length > 0:
            for i in range(length):
                e = self.__darray[i]
                if e >= element:
                    self.__darray.insert(i, element)
                    break
                else:
                    self.__darray.append(element)

        #if list is empty or not sorted, added new element to end
        else:
            self.__darray.append(element)
    
    #D = delete
    def delete(self, element):
        ''' insert new element into array 
            * operation complexity: O(n) **
        '''

        #check if non-empty
        if len(self.__darray) > 0:
            
            #check if element exists
            i = self.search(element)

            if i >= 0:
                self.__darray.remove(element)

    #--- setters and getters ---
    def set_array(self, array):
        self.__darray = array
    
    def get_array(self):
       return self.__darray


def main():
    
    #arg 0 == filename
    for arg in sys.argv[1:]:
        print(arg)

    #create array object
    da = DynamicArray()
    sda = DynamicArray(True)
    
    #insert into array (non sorted)
    print("\nBefore operation (non sorted): {}".format(da.get_array()))
    for x in range(1,4):
        da.insert(x)
    print("After operation: {}".format(da.get_array()))

    #insert into array (non sorted)
    sda.insert(5)
    sda.insert(7)
    print("\nBefore operation (sorted): {}".format(sda.get_array()))
    sda.insert(4)
    sda.insert(6)
    sda.insert(8)
    print("After operation: {}".format(sda.get_array()))

    #search array
    for element in (3,4):
        index = da.search(element)
        print("\nArray: {}".format(da.get_array()))
        print("Element Searched for: {}".format(element))
        print("Index of element: {}".format(index))

    #delete from array
    for element in (3,4):
        print("\nArray: {}".format(da.get_array()))
        print("Element to be delete for: {}".format(element))
        da.delete(element)
        print("After operation: {}".format(da.get_array()))

if __name__ == "__main__":
    main()