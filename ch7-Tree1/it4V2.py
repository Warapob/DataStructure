# class BSTNode:
#     def __init__(self, val=None):
#         self.left = None
#         self.right = None
#         self.val = val

#     def insert(self, val):
#         if not self.val:
#             self.val = val
#             return

#         if self.val == val:
#             return

#         if val < self.val:
#             if self.left:
#                 self.left.insert(val)
#                 return
#             self.left = BSTNode(val)
#             return

#         if self.right:
#             self.right.insert(val)
#             return
#         self.right = BSTNode(val)

#     def get_min(self):
#         current = self
#         while current.left is not None:
#             current = current.left
#         return current.val

#     def get_max(self):
#         current = self
#         while current.right is not None:
#             current = current.right
#         return current.val
    
#     def delete(self, val):
#         if self == None:
#             return self
#         if val < self.val:
#             if self.left:
#                 self.left = self.left.delete(val)
#             return self
#         if val > self.val:
#             if self.right:
#                 self.right = self.right.delete(val)
#             return self
#         if self.right == None:
#             return self.left
#         if self.left == None:
#             return self.right
#         min_larger_node = self.right
#         while min_larger_node.left:
#             min_larger_node = min_larger_node.left
#         self.val = min_larger_node.val
#         self.right = self.right.delete(min_larger_node.val)
#         return self


# def printTree( node, level = 0):
#     if node != None:
#         printTree(node.right, level + 1)
#         print('     ' * level, node.val)
#         printTree(node.left, level + 1)

# T = BSTNode()
# inp = input('Enter Input : ').split(',')
# for i in inp:
#     if i[0] == 'i':
#         print('insert',int(i[2]))
#         root = T.insert(i[2])
#         printTree(T)
#     if i[0] == 'd':
#         print('delete',int(i[2]))
#         if T.val is not None:
#             if T.val == i[2] and T.left == None and T.right == None:
#                 T.val = None
#             else:
#                 root = T.delete(i[2])
#                 printTree(T)
#         else:
#             print('Error! Not Found DATA')


# A class to store a BST node
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
 
# Function to perform inorder traversal on the BST
def inorder(root):
    if root is None:
        return
 
    inorder(root.left)
    print(root.data, end=' ')
    inorder(root.right)
 
 
# Helper function to find minimum value node in the subtree rooted at `curr`
def getMinimumKey(curr):
    while curr.left:
        curr = curr.left
    return curr
 
 
# Recursive function to insert a key into a BST
def insert(root, key):
 
    # if the root is None, create a new node and return it
    if root is None:
        return Node(key)
 
    # if the given key is less than the root node, recur for the left subtree
    if key < root.data:
        root.left = insert(root.left, key)
 
    # if the given key is more than the root node, recur for the right subtree
    else:
        root.right = insert(root.right, key)
 
    return root
 
 
# Function to delete a node from a BST
def deleteNode(root, key):
 
    # pointer to store the parent of the current node
    parent = None
 
    # start with the root node
    curr = root
 
    # search key in the BST and set its parent pointer
    while curr and curr.data != key:
 
        # update the parent to the current node
        parent = curr
 
        # if the given key is less than the current node, go to the left subtree;
        # otherwise, go to the right subtree
        if key < curr.data:
            curr = curr.left
        else:
            curr = curr.right
 
    # return if the key is not found in the tree
    if curr is None:
        print('Error! Not Found DATA')
        return root
 
    # Case 1: node to be deleted has no children, i.e., it is a leaf node
    if curr.left is None and curr.right is None:
 
        # if the node to be deleted is not a root node, then set its
        # parent left/right child to None
        if curr != root:
            if parent.left == curr:
                parent.left = None
            else:
                parent.right = None
 
        # if the tree has only a root node, set it to None
        else:
            root = None
 
    # Case 2: node to be deleted has two children
    elif curr.left and curr.right:
 
        # find its inorder successor node
        successor = getMinimumKey(curr.right)
 
        # store successor value
        val = successor.data
 
        # recursively delete the successor. Note that the successor
        # will have at most one child (right child)
        deleteNode(root, successor.data)
 
        # copy value of the successor to the current node
        curr.data = val
 
    # Case 3: node to be deleted has only one child
    else:
 
        # choose a child node
        if curr.left:
            child = curr.left
        else:
            child = curr.right
 
        # if the node to be deleted is not a root node, set its parent
        # to its child
        if curr != root:
            if curr == parent.left:
                parent.left = child
            else:
                parent.right = child
 
        # if the node to be deleted is a root node, then set the root to the child
        else:
            root = child
 
    return root

def printTree( node, level = 0):
    if node != None:
        printTree(node.right, level + 1)
        print('     ' * level, node.data)
        printTree(node.left, level + 1)


T = None
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[0] == 'i':
        print('insert',int(i[2]))
        T = insert(T,i[2])
        # root = T.insert(i[2])
        printTree(T)
    if i[0] == 'd':
        print('delete',int(i[2]))
        if T is not None:
            T = deleteNode(T,i[2])
            printTree(T)
            # if T.val == i[2] and T.left == None and T.right == None:
            #     T.val = None
            # else:
            #     root = T.delete(i[2])
            #     printTree(T)
        else:
            print('Error! Not Found DATA')