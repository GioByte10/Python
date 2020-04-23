class Node:

    def __init__(self, n):
        self.value = n
        self.parent = None
        self.edges = []
        self.searched = False

    def addEdge(self, neighbor):
        self.edges.append(neighbor)
        neighbor.edges.append(self)

    def __str__(self):
        string = self.value
        for edge in self.edges:
            string += "\n\t" + edge.value
        return string
