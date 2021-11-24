class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    # left nodes are less than root
    # right nodes are more than root
    def __init__(self):
        self.root = Node(None)

    def insert(self, data, node = None):
        if  self.root.data is None:
            self.root = Node(data)
        else:
            node = self.root
            while True:
                if data < node.data:
                    if node.left is None:
                        node.left = Node(data)
                        break
                    node = node.left
                else:
                    if node.right is None:
                        node.right = Node(data)
                        break
                    node = node.right
        return self.root

    def max(self):
        node = self.root
        while True:
            if node.right is None:
                return node.data
            node = node.right

    def min(self):
        node = self.root
        while True:
            if node.left is None:
                return node.data
            node = node.left
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
print("--------------------------------------------------")
print("Min :",T.min())
print("Max :",T.max())