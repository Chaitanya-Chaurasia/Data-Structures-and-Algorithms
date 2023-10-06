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

    def update(self, val1, val2):

        temp = self.head

        # If node with val1 is found, change the val to val2 and break
        # Else, temp = temp.next till temp.next exists

        while temp:
            if temp.val == val1:
                temp.val = val2
                print("Value updated")
                break
            else:
                if temp.next:
                    temp = temp.next
                else: 
                    return


    def deleteHead(self):

        # If no head, return

        if not self.head:
            print("Head not found. Cannot delete!")
            return

        # Else, make the next element the head
        self.head = self.head.next

    def deleteTail(self):
        
        # If head is not found, return
        if not self.head:
            print("Head not found. Cannot Delete!")
            return
        
        # If only head is the node, call delete head
        if self.head.next is None:
            self.deleteHead()
            return

        # ELse travrese till second last element
        # Set next pointer to None
        temp = self.head

        while temp.next.next:
            temp = temp.next
        
        temp.next = None
    
    def deleteAtIndex(self, index):

        # Check if head exists or not
        if not self.head:
            print("Head not found. Cannot Delete!")
            return

        # If index is 0, call deleteHead
        if index == 0:
            self.deleteHead()
            return

        # Else, traverse to (index-1)th position and change next pointers
        curr = 0
        temp = self.head

        while temp.next and curr != index - 1:
            curr += 1
            temp = temp.next

        if temp.next is not None:
            temp.next = temp.next.next
        else:
            print("Invalid index. Cannot Delete!")

    def GetLength(self):

        length = 0
        temp = self.head

        while temp.next:
            length += 1
            temp = temp.next

        print(length + 1)

    def reverseLinkedList(self):

        if not self.head:
            print("Head not found. Cannot reverse LinkedList!")
            return
        else:
            currentNode = self.head
            previousNode = None

            while currentNode:
                nextNode = currentNode.next
                currentNode.next = previousNode
                previousNode = currentNode
                currentNode = nextNode
            self.head = previousNode


    def sortLinkedList(self):
        print("Come back after learning sort")
        

    def printLinkedList(self):

        temp = self.head

        if not temp:
            print("\nNULL")
        while temp:
            print(temp.val , "-> ", end = "")
            if temp.next:
                temp = temp.next
            else:
                print("\n")
                break



list = LinkedList()

list.insertAtBegin(100)
list.insertAtIndex(0, 0)
list.insertAtEnd(200)
list.insertAtIndex(300, 1)
list.insertAtEnd(400)
list.printLinkedList() 

# list.update(200, 300)
# list.printLinkedList() 
# list.deleteAtIndex(0)
# list.printLinkedList()
# list.GetLength() 

list.reverseLinkedList()
list.printLinkedList() 








