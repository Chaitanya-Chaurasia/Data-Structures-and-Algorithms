from collections import deque

import math
class Node:
    # Definition of each node
    
    def __init__(self, left = None, right = None, val = 0):
        self.left = left
        self.right = right
        self.val = val


class BinaryTree:
    # Initialize root as None
    def __init__(self):
        self.root = None

    # Insert at either head or using BST insertion
    def insert(self, val):
        if not self.root:
            self.root = Node(None, None, val)
            print("Root added!")
        else: 
            self.BSTinsert(val, self.root)
        
    def BSTinsert(self, val, node):
        
        # If val is less, add to left subtree
        if val < node.val:
            if node.left:
                self.BSTinsert(val, node.left)
            else:
                node.left = Node(None, None, val)
        # else, add to right subtree
        else:
            if node.right:
                self.BSTinsert(val, node.right)
            else:
                node.right = Node(None, None, val)

    
    # Find an element using recursive calls

    def search(self, val) -> Node:
        if not self.root:
            print("Root is NULL! Cannot search!")
            return None
        
        else:
            return self.BSTsearch(val, self.root)
            
    def BSTsearch(self, val, node) -> Node:

        if node is None or val == node.val:
            return node
        
        if val < node.val:
            return self.BSTsearch(val, node.left)
        else: 
            return self.BSTsearch(val, node.right)
        
    def BSTdelete(self, root, val):

        if root is None: 
            return root
        
        elif val < root.val:
            root.left = self.BSTdelete(root.left, val)
        elif val > root.val:
            root.right = self.BSTdelete(root.right, val)
        else:

            if root.left is None and root.right is None:
                del root
                return root
            elif root.left is None:
                temp = root
                root = root.right
                return root
            elif root.right is None:
                temp = root
                root = root.left
                return root
            else:
                temp = self.findSuccessor(root.right)
                root.val = temp.val
                root.right = self.BSTdelete(root.right, temp.val)


    def findSuccessor(self, root) -> Node:

        while root.left:
            root = root.left

        return root
    
    # Implemented DFS using stack
    # Declare a stack, and add root to it.

    # Pop the stack
    # Append children to the stack
    # Print the parent
    # Do this iteratively for each element in the stack, while stack is not empty

    def DFS(self):

        stack = []
        temp_root = self.root
        stack.append(temp_root)
        

        while len(stack) > 0:
            
            temp = stack.pop()

            if temp.left:
                stack.append(temp.left)
            if temp.right:
                stack.append(temp.right)
            
            print(str(temp.val) + " ", end = "")
              
    
    # Implemented BFS using queue (deque from collections)

    def BFS(self):

        queue = deque()
        temp_root = self.root
        queue.append(temp_root)

        while len(queue) > 0: 

            temp = queue.popleft()

            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)

            print(str(temp.val) + " ", end = " ")
    
    # Different traversal algorithms

    def inorderTraversal(self, temp):
    
        if not temp:
            return 
        
        node = temp
        self.printTree(node.left)
        print(node.val)
        self.printTree(node.right)

    def postorderTraversal(self, temp):
    
        if not temp:
            return 
        
        node = temp
        self.printTree(node.left)
        self.printTree(node.right)
        print(node.val)

    def preorderTraversal(self, temp):
    
        if not temp:
            return 
        
        node = temp
        print(node.val)
        self.printTree(node.left)
        self.printTree(node.right)
        


tree = BinaryTree()
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(-1)

tree.BSTdelete(tree.root, 1)
tree.BFS()
print("\n")
tree.DFS()
print("\n")






    
    
