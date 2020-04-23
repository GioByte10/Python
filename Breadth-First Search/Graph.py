class Graph:

    def __init__(self):
        self.nodes = []
        self.graph = []
        self.start = None
        self.end = None


    def addNode(self, node):
        self.nodes.append(node)
        self.graph.append(node)


    def getNode(self, nodeValue):
        for node in self.nodes:
            if node.value == nodeValue:
                return node

        return None


    def setStart(self, start):
        for node in self.nodes:
            if node.value == start:
                self.start = node

        return self.start


    def setEnd(self, end):
        for node in self.nodes:
            if node.value == end:
                self.end = node

        return self.end


    def __str__(self):
        string = ""
        for node in self.nodes:
            string += str(node) + "\n\n"

        return string
