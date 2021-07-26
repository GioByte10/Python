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
        self.walls = [True, True, True, True]
        self.visited = False


    def show(self):
        w = Cell.width
        h = Cell.height

        x = self.x * w
        y = self.y * h

        if self.visited:
            Cell.c.create_rectangle(x, y, x + w, y + h, fill="gray", outline="")

        if self.walls[0]:
            Cell.c.create_line(x, y, x + w, y, fill="white")

        if self.walls[1]:
            Cell.c.create_line(x + w, y, x + w, y + h, fill="white")

        if self.walls[2]:
            Cell.c.create_line(x + w, y + h, x, y + h, fill="white")

        if self.walls[3]:
            Cell.c.create_line(x, y + h, x, y, fill="white")


    def getNeighbor(self):
        neighbors = []

        col = self.x
        row = self.y

        top = None
        right = None
        bottom = None
        left = None

        if col > 0:
            top = Cell.grid[(col - 1) + row * Cell.cols]

        if row < Cell.rows - 1:
            right = Cell.grid[col + (row + 1) * Cell.cols]

        if col < Cell.cols - 1:
            bottom = Cell.grid[(col + 1) + row * Cell.cols]

        if row > 0:
            left = Cell.grid[col + (row - 1) * Cell.cols]

        if top is not None and not top.visited:
            neighbors.append(top)

        if right is not None and not right.visited:
            neighbors.append(right)

        if bottom is not None and not bottom.visited:
            neighbors.append(bottom)

        if left is not None and not left.visited:
            neighbors.append(left)

        if len(neighbors) > 0:
            return neighbors[random.randint(0, len(neighbors) - 1)]

        return None

    def highlight(self):
        w = Cell.width
        h = Cell.height

        x = self.x * w
        y = self.y * h

        Cell.c.create_rectangle(x, y, x + w, y + h, fill="purple", outline="")


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
