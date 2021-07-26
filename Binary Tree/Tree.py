from Node import Node


class Tree:

    def __init__(self):
        self.root = None

    def addNode(self, n):
        node = Node(n)
        if self.root is None:
            self.root = node
        else:
            self.root.addValue(node)
