class Node:

    def __init__(self, n):
        self.node = n
        self.left = None
        self.right = None

    def addValue(self, n):
        if n.node < self.node:
            if self.left is None:
                self.left = n
            else:
                self.left.addValue(n)

        elif n.node > self.node:
            if self.right is None:
                self.right = n
            else:
                self.right.addValue(n)

    def showTree(self):
        if self.left is not None:
            self.left.showTree()

        print(self.node)

        if self.right is not None:
            self.right.showTree()

    def findNode(self, node):

        print(str(self.node))

        if self.node == node:
            print("Found " + str(node))

        elif self.left is not None and node < self.node:
            self.left.findNode(node)

        elif self.right is not None and node > self.node:
            self.right.findNode(node)
