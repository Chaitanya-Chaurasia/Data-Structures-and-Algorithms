# Heaps are implemented using a tree like structure, but in an array
# The max/min element is always on the top.

# If our array is 1| 2| 3| 5| 5, root is A[0]
# Children are located at index 2*i + 1 and 2*i + 2 index.
# Hence for every element, parent is A[i - 1/2].

# Below is the implementation of a min heap. We can easily modify this to form a max heap

import sys

class MinHeap():

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.heap = [0]* (self.maxsize + 1)
        self.heap[0] = -1*maxsize
        self.size = 0

    def parent(self, i):
        return i//2
    
    def leftChild(self, i):
        return 2*i
    
    def rightChild(self, i):
        return 2*i + 1
    
    def isLeaf(self, i):
        return i*2 > self.size

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insertValue(self, value):
        
        # If max size exceeds, return
        if self.size >= sys.maxsize:
            print("HEAP SIZE Limit reached")
            return
        
        # Else, inscrement size by 1
        self.size += 1

        # Add value as the last element of the heap
        self.heap[self.size] = value

        # Keep on swapping with the parent, if it is lesser than the new value 
        current = self.size
        
        print(int(self.heap[self.parent(current)]))
        while self.heap[current] < self.heap[self.parent(current)]: 
            self.swap(current, self.parent(current)) 
            current = self.parent(current) 

        # But even after this, it is not guaranteed that all elements are in there correct position. We will have to check the position of each parent and check if it is lesser than its children.

    def minHeap(self):
        
        # This function will convert existing array into a heap.
        # We only need to iterate over the the first size//2 elements.
        # because the next size//2 elements are the children in form of leaves.

        for i in range(self.size//2, 0, -1):
            self.heapify(i)
    
    def heapify(self, index):
        
        if not self.isLeaf(index):
            if self.heap[index] > (self.heap[self.leftChild(index)] or self.heap[self.rightChild(index)]):

                if self.heap[self.leftChild(index)] > self.heap[self.rightChild(index)]:
                    self.swap(index, self.rightChild(index))
                    self.heapify(self.rightChild(index))
                else:
                    self.swap(index, self.leftChild(index))
                    self.heapify(self.leftChild(index))


    def printHeap(self):
        print(self.heap)

heap = MinHeap(10)
heap.insertValue(10)
heap.insertValue(5)
heap.printHeap()

