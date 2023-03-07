# import os library
import os
from os.path import exists as file_exists
# Python3 program to implement
# a queue using an array
import fileinput
import numpy as np
from secrets import choice

class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class SortedLinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    def insert(self, newNode):
        # Special case for the empty linked list
        if self.head is None:
            newNode.next = self.head
            self.head = newNode

        # Special case for head at end
        elif self.head.data > newNode.data:
            newNode.next = self.head
            self.head = newNode

        # Locate the node before the point of insertion
        else :
            current = self.head
            while(current.next is not None and current.next.data < newNode.data):
                current = current.next
            if current.data == newNode.data:
                return # ignore duplicates
            if (current.next is not None and current.next.data == newNode.data):
                return # ignore duplicates
            newNode.next = current.next
            current.next = newNode

    # Given a reference to the head of a
    # list and a key, remove the first
    # occurrence of key in sorted linked list
    def remove(self, key):
        # Store head node
        temp = self.head
 
        # If head node itself holds the
        # key to be removed
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
 
        # Search for the key to be removed,
        # keep track of the previous node as
        # we need to change 'prev.next'
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
 
        # if key was not present in
        # sorted linked list
        if(temp == None):
            print("Key", key, "is not present")
            return
 
        # Unlink the node from sorted linked list
        prev.next = temp.next
        temp = None


    # This Function checks whether the value
    # x present in the sorted linked list
    def search(self, x):
        # Initialize current to head
        current = self.head
 
        # loop till current not equal to None
        while current != None:
            if current.data == x:
                return True  # data found
            current = current.next
 
        return False  # Data Not found

    # Utility function to print the SortedLinkedList
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end = "->")
            temp = temp.next
        print()

class Queue:

	# To initialize the object.
	def __init__(self, c):

		self.queue = []
		self.front = self.rear = 0
		self.capacity = c

	# Function to insert an element
	# at the rear of the queue
	def queueEnqueue(self, data):

		# Check queue is full or not
		if(self.capacity == self.rear):
			print("\nQueue is full")

		# Insert element at the rear
		else:
			self.queue.append(data)
			self.rear += 1

	# Function to delete an element
	# from the front of the queue
	def queueDequeue(self):

		# If queue is empty
		if(self.front == self.rear):
			print("Queue is empty")

		# Pop the front element from list
		else:
			x = self.queue.pop(0)
			self.rear -= 1

	# Function to print queue elements
	def queueDisplay(self):

		if(self.front == self.rear):
			print("\nQueue is Empty")

		# Traverse front to rear to
		# print elements
		for i in self.queue:
			print(i, "<--", end='')

	# Print front of queue
	def queueFront(self):

		if(self.front == self.rear):
			print("\nQueue is Empty")

		print("\nFront Element is:",
			self.queue[self.front])


sSortedLinkedListObj = SortedLinkedList()

def inputIntoSortedLinkedListFromFile():
    while True:
        print("Current menu selected is 7 i.e, Input into Sorted List from File")
        print("Enter file name to proceed or back to go to main menu:")
        text = input()
        # If input is back go back to main menu
        if "back" in text:
            break
        # Else if input file exist then process
        elif file_exists(text):
            fileObj = open(text, "r")
            for currentLine in fileObj:
                splits = currentLine.split(',')
                for split in splits:
                    flag = True
                    try:
                        split = int(split.strip()) # strip all right and left space
                    except ValueError:
                        flag = False # ignore all alphabets, decimals, special characters
                    if flag:
                        newNode = Node(split)
                        sSortedLinkedListObj.insert(newNode)
            fileObj.close()
            sSortedLinkedListObj.display()
        # Else throw error
        else:
            print("File does not exist or invalid input")

def inputIntoSortedLinkedListFromCmdLine():
    while True:
        print("Current menu selected is 8 i.e, Input into Sorted List from command line")
        print("Enter a single integer or comma separated integers to proceed or back to go to main menu:")
        text = input()
        # If input is back go back to main menu
        if "back" in text:
            break
        # Else process the input
        else:
            splits = text.split(',')
            for split in splits:
                flag = True
                try:
                    split = int(split.strip()) # strip all right and left space
                except ValueError:
                    flag = False # ignore all alphabets, decimals, special characters
                if flag:
                    newNode = Node(split)
                    sSortedLinkedListObj.insert(newNode)
            sSortedLinkedListObj.display()

def searchElementFromSortedLinkedList():
    while True:
        print("Current menu selected is 9 i.e, Find element in Sorted List")
        print("Enter a single integer to search or back to go to main menu:")
        text = input()
        # If input is back go back to main menu
        if "back" in text:
            break
        # Else process the input
        else:
            flag = True
            try:
                text = int(text.strip()) # strip all right and left space
            except ValueError:
                print("Invalid choice")
                flag = False # ignore all alphabets, decimals, special characters
            if flag:
                print("Key", text, "found") if True == sSortedLinkedListObj.search(text) else print("Key", text, "not found")

def removeElementFromSortedLinkedList():
    while True:
        print("Current menu selected is 10 i.e, Remove element in Sorted List")
        print("Enter a single integer to remove or back to go to main menu:")
        text = input()
        # If input is back go back to main menu
        if "back" in text:
            break
        # Else process the input
        else:
            flag = True
            try:
                text = int(text.strip()) # strip all right and left space
            except ValueError:
                print("Invalid choice")
                flag = False # ignore all alphabets, decimals, special characters
            if flag:
                sSortedLinkedListObj.remove(text)
                sSortedLinkedListObj.display()

def inputIntoArrayFromFile():
    arrayFile = []
    with open('/Users/arrd/Documents/MTech/Course/Data structure/Assignment/example.txt') as f:
        str_arr = ','.join([l.strip() for l in f])

        arrayFile = np.asarray(str_arr.split(','), dtype=int)

        n = len(arrayFile)
        q = Queue(n)

        # Inserting elements in the queue
        for i in arrayFile:
            q.queueEnqueue(i)
            
def inputIntoArrayFromCmd():
    # Create a new queue of capacity n
    q = Queue(int(input("Enter the size of the queue: ")))

    # Inserting elements in the queue
    q.queueEnqueue(int(input("Enter the element to push: ")))
        
            
        
def deleteFromArray():
    # Deleting element from the queue
    q = Queue()
    q.queueDequeue()
     

# infinite while loop
while True:
    print("Choose a +ve integer from below menu items :-")
    print("1. Input into Array Queue from File (Multiple elements)")
    print("2. Input into Array Queue from command line (Single Element)")
    print("3. Remove element from Array Queue (Single Element)")
    print("4. Input into List Queue from File")
    print("5. Input into List Queue from command line")
    print("6. Remove element from List Queue")
    print("7. Input into Sorted List from File")
    print("8. Input into Sorted List from command line")
    print("9. Find element in Sorted List")
    print("10. Remove element in Sorted List")
    print("11. Input into BST from File")
    print("12. Input into BST from command line")
    print("13. Find element in BST")
    print("14. Remove element From BST")
    print("15. Print BST in order")
    print("16. Quit")

    # take input from user
    choice = input()

    if (0 == choice.isdigit()):
        print("Invalid choice")
        continue

    choice = int(choice)

    if (1 == choice):
        inputIntoArrayFromCmd()
    elif (2 == choice):
        inputIntoArrayFromCmd()
    elif (3 == choice):
        deleteFromArray()
    elif (4 == choice):
        print("Selected 4")
    elif (5 == choice):
        print("Selected 5")
    elif (6 == choice):
        print("Selected 6")
    elif (7 == choice):
        inputIntoSortedLinkedListFromFile()
    elif (8 == choice):
        inputIntoSortedLinkedListFromCmdLine()
    elif (9 == choice):
        searchElementFromSortedLinkedList()
    elif (10 == choice):
        removeElementFromSortedLinkedList()
    elif (11 == choice):
        print("Selected 11")
    elif (12 == choice):
        print("Selected 12")
    elif (13 == choice):
        print("Selected 13")
    elif (14 == choice):
        print("Selected 14")
    elif (15 == choice):
        print("Selected 15")
    elif (16 == choice):
        print("Thank you!")
        break
    else :
        print("Invalid choice")
