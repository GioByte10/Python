import random


class Cell:
    c = None
    rows = 0
    cols = 0
    width = 0
    height = 0
    grid = []

    def __init__(self, row, col):
        self.x = col
        self.y = row
        self.square = None
        self.top = None
        self.right = None
        self.bottom = None
        self.left = None
        self.walls = [True, True, True, True]
        self.visited = False


    def show(self):
        w = Cell.width
        h = Cell.height

        x = self.x * w
        y = self.y * h

        if self.walls[0]:
            self.top = Cell.c.create_line(x, y, x + w, y, fill="white")

        if self.walls[1]:
            self.right = Cell.c.create_line(x + w, y, x + w, y + h, fill="white")

        if self.walls[2]:
            self.bottom = Cell.c.create_line(x + w, y + h, x, y + h, fill="white")

        if self.walls[3]:
            self.left = Cell.c.create_line(x, y + h, x, y, fill="white")


    def getNeighbor(self):
        neighbors = []
        tempNeighbors = []

        col = self.x
        row = self.y

        if col < Cell.cols - 1:
            tempNeighbors.append(Cell.grid[row][col + 1])

        if col > 0:
            tempNeighbors.append(Cell.grid[row][col - 1])

        if row < Cell.rows - 1:
            tempNeighbors.append(Cell.grid[row + 1][col])

        if row > 0:
            tempNeighbors.append(Cell.grid[row - 1][col])

        for neighbor in tempNeighbors:
            if not neighbor.visited:
                neighbors.append(neighbor)

        if len(neighbors) > 0:
            neighbor = neighbors[random.randint(0, len(neighbors) - 1)]
            neighbor.visited = True
            neighbor.changeColor()

            return neighbor

        return None


    def changeColor(self):
        w = Cell.width
        h = Cell.height

        x = self.x * w
        y = self.y * h

        Cell.c.create_rectangle(x, y, x + w, y + h, fill="gray", outline="")


''' def addNeighbors(self):
        col = self.x
        row = self.y

        if col < Cell.cols - 1:
            self.neighbors.append(Cell.grid[row][col + 1])
        if col > 0:
            self.neighbors.append(Cell.grid[row][col - 1])
        if row < Cell.rows - 1:
            self.neighbors.append(Cell.grid[row + 1][col])
        if row > 0:
            self.neighbors.append(Cell.grid[row - 1][col])
'''
