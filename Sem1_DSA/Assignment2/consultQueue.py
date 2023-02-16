# Python3 implementation of Max Heap
import sys
from patientNode import PatientNode

class MaxHeap:

    def __init__(self, size):

        self.maxsize = size
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        # self.Heap[0] = PatientNode('Zero',9999,000)
        self.Heap[0] = sys.maxsize
        self.FRONT = 1

    # Function to return the position of
    # parent for the node currently
    # at pos
    def parent(self, pos):

        return pos // 2

    # Function to return the position of
    # the left child for the node currently
    # at pos
    def leftChild(self, pos):

        return 2 * pos

    # Function to return the position of
    # the right child for the node currently
    # at pos
    def rightChild(self, pos):

        return (2 * pos) + 1

    # Function that returns true if the passed
    # node is a leaf node
    def isLeaf(self, pos):

        if pos >= (self.size // 2) and pos <= self.size:
            return True
        return False

    # Function to swap two nodes of the heap
    def swap(self, fpos, spos):

        self.Heap[fpos], self.Heap[spos] = (self.Heap[spos], self.Heap[fpos])

    # Function to heapify the node at pos
    def maxHeapify(self, pos):

        # If the node is a non-leaf node and smaller
        # than any of its child
        if not self.isLeaf(pos):
            if (self.Heap[pos] < self.Heap[self.leftChild(pos)]
                    or self.Heap[pos] < self.Heap[self.rightChild(pos)]):

                # Swap with the left child and heapify
                # the left child
                if (self.Heap[self.leftChild(pos)] >
                        self.Heap[self.rightChild(pos)]):
                    self.swap(pos, self.leftChild(pos))
                    self.maxHeapify(self.leftChild(pos))

                # Swap with the right child and heapify
                # the right child
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.maxHeapify(self.rightChild(pos))

    # Function to insert a node into the heap
    def insert(self, element):

        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element

        current = self.size
        par = self.parent(current)

        print(current)
        print(par)

    
       
        if(current != 1 and par != 0):
            while (self.Heap[current].age > self.Heap[self.parent(current)].age):
                self.swap(current, self.parent(current))
                current = self.parent(current)

    # Function to print the contents of the heap
    def Print(self):

        for i in range(1, (self.size // 2) + 1):
            # print("PARENT:" + str(self.Heap[i]) + " " + "LEFT CHILD:" +
            #       str(self.Heap[2 * i]) + " " + "RIGHT CHILD:" +
            #       str(self.Heap[2 * i + 1]) + " ")
            print("PARENT:" + str(self.Heap[i].patient_id if self.Heap[i] != 0 else self.Heap[i] ) + " " + "LEFT CHILD:" +
                  str(self.Heap[2 * i].patient_id if self.Heap[2 * i] != 0 else self.Heap[2 * i]) + " " + "RIGHT CHILD:" +
                  str(self.Heap[2 * i + 1].patient_id if self.Heap[2 * i + 1] != 0 else self.Heap[2 * i + 1]) + " ")

        print(self.Heap)

    # Function to remove and return the maximum
    # element from the heap
    def extractMax(self):

        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.maxHeapify(self.FRONT)

        return popped.patient_id


# Driver Code
if __name__ == "__main__":
    sampleNode = PatientNode('Abc',55,123)
    sampleNode2 = PatientNode('Def',57,124)
    print('The maxHeap is ')

    maxHeap = MaxHeap(15)
    maxHeap.insert(sampleNode)
    maxHeap.insert(sampleNode2)
    # maxHeap.insert(3)
    # maxHeap.insert(17)
    # maxHeap.insert(10)
    # maxHeap.insert(84)
    # maxHeap.insert(19)
    # maxHeap.insert(19)
    # maxHeap.insert(6)
    # maxHeap.insert(22)
    # maxHeap.insert(9)
    # maxHeap.insert(99)
    # maxHeap.insert(99)

    maxHeap.Print()

    # print("The Next patient is " + str(maxHeap.extractMax()))
    # maxHeap.Print()
    # print("The Next patient is " + str(maxHeap.extractMax()))
    # maxHeap.Print()
    # print("The Next patient is " + str(maxHeap.extractMax()))
    # maxHeap.Print()
    # print("The Next patient is " + str(maxHeap.extractMax()))
    # maxHeap.Print()
    # print("The Next patient is " + str(maxHeap.extractMax()))
    # maxHeap.Print()
    # print("The Next patient is " + str(maxHeap.extractMax()))