
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def insertAtBegin(self, val):

        # If head does not exist, create a new head
        if self.head is None:
            self.head = Node(val)
            return
        
        # If head already exists, follow the steps:
        # 1. Create a new temp node
        # 2. Make its next pointer point to head
        # 3. Make it the head

        else: 
            newHead = Node(val)
            newHead.next = self.head
            self.head = newHead

    def insertAtEnd(self, val):

        # Traverse to the last element, given that the list is not empty
        # Once done, add a new node as the next pointer to the last node

        if self.head:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(val)

        else: 
            print("Head is NULL. Calling insertAtBegin()")
            self.insertAtBegin(val)

    def insertAtIndex(self, val, index):

        curr = 0
        temp = self.head
        
        # If index is 0 or head is NULL, call insertAtBegin
        if index == 0 or not self.head:
            self.insertAtBegin(val)
        
        
        # If index > 0, loop till index - 1.
        # Once found, check if current element is NULL or not
        # If null, index not found.
        # Else, change pointers
        else:
            while temp and curr != index - 1:
                curr += 1
                temp = temp.next

            newNode = Node(val)

            if temp:
                newNode.next = temp.next
                temp.next = newNode

            else:
                print("Index out of range")

    # def update(self, val):

    # def deleteHead(self, val):

    # def deleteTail(self, val):

    # def deleteAtIndex(self, val, index):

    # def GetLength(self):


    def printLinkedList(self):

        while self.head:
            print(self.head.val , "->")
            self.head = self.head.next



list = LinkedList()

list.insertAtEnd(100)
list.printLinkedList() 







