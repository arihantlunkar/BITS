# import os library
import os
from os.path import exists as file_exists

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

sSortedLinkedListObj = SortedLinkedList()

#BST
class BSTNode:
    #Each node in BST should have Value, Left & Right
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val: #Initial case when BST is empty / not defined
            self.val = val 
            return

        if self.val == val: #Case for duplicates
            return

        if val < self.val: #When value is lesser, insert to left sub tree
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right: #When value is higher, insert to right sub tree
            self.right.insert(val)
            return
        self.right = BSTNode(val)

    def delete(self, val):
        if not self.val: #When BST is not defined
            return

        if val < self.val: #Find if present in left sub tree
            if self.left:
                self.left = self.left.delete(val)
            return self
        if val > self.val: #Find if present in right sub tree
            if self.right:
                self.right = self.right.delete(val)
            return self
        #Reorder values after deletion
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self

    def exists(self, val):
        #Initial case when BST is empty
        if not self.val:
            return False
    
        if val == self.val: #Found
            return True

        if val < self.val: #Find in left sub tree
            if self.left == None:
                return False
            return self.left.exists(val)

        if self.right == None: #Find in right sub tree
            return False
        return self.right.exists(val)

    def preorder(self, vals):
        if self.val is not None:
            vals.append(self.val) #self
        if self.left is not None:
            self.left.preorder(vals) #left
        if self.right is not None:
            self.right.preorder(vals) #right
        return vals

    def inorder(self, vals):
        if self.left is not None:
            self.left.inorder(vals) #left
        if self.val is not None:
            vals.append(self.val) #self
        if self.right is not None:
            self.right.inorder(vals) #right
        return vals
    
    def postorder(self, vals):
        if self.left is not None:
            self.left.postorder(vals) #left
        if self.right is not None:
            self.right.postorder(vals) #right
        if self.val is not None:
            vals.append(self.val) #self
        return vals

BSTObj = BSTNode()    

class Queue:

	# To initialize the object.
	def __init__(self):

		self.queue = []
		self.front = self.rear = 0

	# Function to delete an element
	# from the front of the queue
	def queueEnqueue(self, data):

		# If queue is empty
		if(data in self.queue):
			return

		# Push the element into the list
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

qObj= Queue()

class QueueLinkedList:

	# To initialize the object.
	def __init__(self):

		self.head = None
		self.tail = None
		self.count = 0

	# Function to delete an element
	# from the front of the queue
	def queueEnqueue(self, data):

		newNode = Node(data)
		newNode.next = None
        
		# If queueLinkedList is empty
		if self.head is None:
			self.head = newNode
			self.tail = newNode
			self.count = 1
			return

		# Push the element into the list
		else:
			self.tail.next = newNode
			self.tail = newNode
			self.count += 1


	# Function to delete an element
	# from the front of the queue
	def queueDequeue(self):

		# If queueLinkedList is empty
		if self.head is None:
			print("Queue is empty")

		# Pop the front element from list
		else:
			x = self.head
			self.head = self.head.next
			if self.head is None :
				self.tail = None
			self.count -= 1

	# Function to print queuelinkedList elements
	def queueDisplay(self):

		if self.head is None:
			print("\nQueue is Empty")

		# Traverse front to rear to
		# print elements
		current = self.head
		while current is not None:
			print(current.data, "<--", end='')
			current = current.next
            

qListObj= QueueLinkedList()


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

def inputIntoBSTFromFile():
    while True:
        print("Current menu selected is 11 i.e, Input into BST from File")
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
                        BSTObj.insert(split)
            fileObj.close()
            print("BST 'pre-order:'")
            print(BSTObj.preorder([]))
        # Else throw error
        else:
            print("File does not exist or invalid input")

def inputIntoBSTFromCmdLine():
    while True:
        print("Current menu selected is 12 i.e, Input into BST from command line")
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
                    BSTObj.insert(split)
                print("BST 'post-order:'")
                print(BSTObj.postorder([]))

def findElementInBST():
    while True:
        print("Current menu selected is 13 i.e, Find element in BST")
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
                print("Key", text, "found") if True == BSTObj.exists(text) else print("Key", text, "not found")

def removeElementFromBST():
    while True:
        print("Current menu selected is 14 i.e, Remove element in BST")
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
                if BSTObj.exists(text):
                    BSTObj.delete(text)
                    print(BSTObj.inorder([]))
                else:
                    print("Key", text, "not found")

def printBSTInorder():
    while True:
        print("Current menu selected is 15 i.e, Print BST in order")
        # print(BSTObj.inorder([]))
        print("Enter 0 to print the BST in order or back to go to main menu:")
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
                if text == 0:
                    print(BSTObj.inorder([]))

def inputIntoArrayFromFile():
    while True:
        print("Current menu selected is 1 i.e, Input into Queue from File")
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
                        qObj.queueEnqueue(split)
            fileObj.close()
            qObj.queueDisplay()
            print("\n")
       # Else throw error
        else:
            print("File does not exist or invalid input")

def inputIntoArrayQueueFromCmdLine():
    while True:
        print("Current menu selected is 2 i.e, Input into Array queue from command line")
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
                    qObj.queueEnqueue(split)

            qObj.queueDisplay()
            print("\n")


def removeElementFromArrayQueue():
    print("Current menu selected is 3 i.e, Remove element in Queue")
    qObj.queueDequeue()
    qObj.queueDisplay()
    print("\n")

def inputIntoListFromFile():
    while True:
        print("Current menu selected is 4 i.e, Input into Queue from File")
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
                        qListObj.queueEnqueue(split)
            fileObj.close()
            qListObj.queueDisplay()
            print("\n")
       # Else throw error
        else:
            print("File does not exist or invalid input")

def inputIntoListQueueFromCmdLine():
    while True:
        print("Current menu selected is 5 i.e, Input into List queue from command line")
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
                    qListObj.queueEnqueue(split)

            qListObj.queueDisplay()
            print("\n")
            


def removeElementFromListQueue():
    print("Current menu selected is 6 i.e, Remove element in QueueLinkedList")
    qListObj.queueDequeue()
    qListObj.queueDisplay()
    print("\n")

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
        inputIntoArrayFromFile()
    elif (2 == choice):
        inputIntoArrayQueueFromCmdLine()
    elif (3 == choice):
        removeElementFromArrayQueue()
    elif (4 == choice):
        inputIntoListFromFile()
    elif (5 == choice):
        inputIntoListQueueFromCmdLine()
    elif (6 == choice):
        removeElementFromListQueue()
    elif (7 == choice):
        inputIntoSortedLinkedListFromFile()
    elif (8 == choice):
        inputIntoSortedLinkedListFromCmdLine()
    elif (9 == choice):
        searchElementFromSortedLinkedList()
    elif (10 == choice):
        removeElementFromSortedLinkedList()
    elif (11 == choice):
        inputIntoBSTFromFile() 
    elif (12 == choice):
        inputIntoBSTFromCmdLine()
    elif (13 == choice):
        findElementInBST()
    elif (14 == choice):
        removeElementFromBST()
    elif (15 == choice):
        printBSTInorder()
    elif (16 == choice):
        print("Thank you!")
        break
    else :
        print("Invalid choice")