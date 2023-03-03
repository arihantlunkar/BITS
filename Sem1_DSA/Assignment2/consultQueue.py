# Python3 implementation of Max Heap
import sys
from patientNode import PatientNode
#import heapq

# class MaxHeap:

#     def __init__(self, size):

#         self.maxsize = size
#         self.size = 0
#         self.Heap = [0] * (self.maxsize + 1)
#         self.Heap[0] = PatientNode('Zero',9999,000)
#         #self.Heap[0] = sys.maxsize
#         self.FRONT = 1

#     # Function to return the position of
#     # parent for the node currently
#     # at pos
#     def parent(self, pos):

#         return pos // 2

#     # Function to return the position of
#     # the left child for the node currently
#     # at pos
#     def leftChild(self, pos):

#         return 2 * pos

#     # Function to return the position of
#     # the right child for the node currently
#     # at pos
#     def rightChild(self, pos):

#         return (2 * pos) + 1

#     # Function that returns true if the passed
#     # node is a leaf node
#     def isLeaf(self, pos):

#         if pos >= (self.size // 2) and pos <= self.size:
#             return True
#         return False

#     # Function to swap two nodes of the heap
#     def swap(self, fpos, spos):

#         self.Heap[fpos], self.Heap[spos] = (self.Heap[spos], self.Heap[fpos])

#     # Function to heapify the node at pos
#     def maxHeapify(self, pos):

#         # If the node is a non-leaf node and smaller
#         # than any of its child
#         if not self.isLeaf(pos):
#             if (self.Heap[pos].age < self.Heap[self.leftChild(pos)].age
#                     or self.Heap[pos].age < self.Heap[self.rightChild(pos)].age):

#                 # Swap with the left child and heapify
#                 # the left child
#                 if (self.Heap[self.leftChild(pos)].age >
#                         self.Heap[self.rightChild(pos)].age):
#                     self.swap(pos, self.leftChild(pos))
#                     self.maxHeapify(self.leftChild(pos))

#                 # Swap with the right child and heapify
#                 # the right child
#                 else:
#                     self.swap(pos, self.rightChild(pos))
#                     self.maxHeapify(self.rightChild(pos))

#     # Function to insert a node into the heap
#     def insert(self, element):

#         if self.size >= self.maxsize:
#             return
#         self.size += 1
#         self.Heap[self.size] = element

#         current = self.size

#         while (self.Heap[current].age > self.Heap[self.parent(current)].age):
#             self.swap(current, self.parent(current))
#             current = self.parent(current)

#     # Function to print the contents of the heap
#     def Print(self):

#         for i in range(1, (self.size // 2) + 1):
#             # print("PARENT:" + str(self.Heap[i]) + " " + "LEFT CHILD:" +
#             #       str(self.Heap[2 * i]) + " " + "RIGHT CHILD:" +
#             #       str(self.Heap[2 * i + 1]) + " ")
#             print("PARENT:" + str(self.Heap[i].patient_id if self.Heap[i] != 0 else self.Heap[i] ) + " " + "LEFT CHILD:" +
#                   str(self.Heap[2 * i].patient_id if self.Heap[2 * i] != 0 else self.Heap[2 * i]) + " " + "RIGHT CHILD:" +
#                   str(self.Heap[2 * i + 1].patient_id if self.Heap[2 * i + 1] != 0 else self.Heap[2 * i + 1]) + " ")

#         print(self.Heap)

#     # Function to remove and return the maximum
#     # element from the heap
#     def extractMax(self):

#         popped = self.Heap[self.FRONT]
#         self.Heap[self.FRONT] = self.Heap[self.size]
#         self.size -= 1
#         self.maxHeapify(self.FRONT)

#         return popped

# class Patient:
#     def __init__(self, name, age, patient_id):
#         self.name = name
#         self.age = age
#         self.patient_id = patient_id
    
#     def __lt__(self, other):
#         if self.age == other.age:
#             return self.patient_id < other.patient_id
#         return self.age > other.age
    
#     def __repr__(self):
#         return f"Patient(name='{self.name}', age={self.age}, patient_id={self.patient_id})"

# class MaxHeap:
#     def __init__(self):
#         self._heap = []
    
#     def push(self, patient):
#         heapq.heappush(self._heap, patient)
    
#     def extract_max(self):
#         return heapq.heappop(self._heap)
    
#     def peek_max(self):
#         return self._heap[0]
    
#     def __len__(self):
#         return len(self._heap)

class MaxHeap:
    def __init__(self):
        self._heap = []
        
    def enqueuePatient(self, patient):
        self._heap.append(patient)
        self._sift_up(len(self._heap) - 1)
        
    def extract_max(self):
        if len(self._heap) == 0:
            return None
        max_patient = self._heap[0]
        last_patient = self._heap.pop()
        if len(self._heap) > 0:
            self._heap[0] = last_patient
            self._sift_down(0)
        return max_patient
    
    def peek_max(self):
        if len(self._heap) == 0:
            return None
        return self._heap[0]
    
    def __len__(self):
        return len(self._heap)
    
    def _sift_up(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self._is_better(self._heap[index], self._heap[parent_index]):
            self._heap[index], self._heap[parent_index] = self._heap[parent_index], self._heap[index]
            index = parent_index
            parent_index = (index - 1) // 2
        
    def _sift_down(self, index):
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            max_index = index
            if left_child_index < len(self._heap) and self._is_better(self._heap[left_child_index], self._heap[max_index]):
                max_index = left_child_index
            if right_child_index < len(self._heap) and self._is_better(self._heap[right_child_index], self._heap[max_index]):
                max_index = right_child_index
            if max_index == index:
                break
            self._heap[index], self._heap[max_index] = self._heap[max_index], self._heap[index]
            index = max_index
        
    def _is_better(self, patient_a, patient_b):
        if patient_a.age != patient_b.age:
            return patient_a.age > patient_b.age
        else:
            return patient_a.patient_id > patient_b.patient_id
