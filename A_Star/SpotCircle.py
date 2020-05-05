import random


class SpotCircle:
    rows = 0
    cols = 0
    height = 0
    width = 0
    c = 0
    grid = 0

    def __init__(self, row, col):
        self.x = col
        self.y = row
        self.g = 0
        self.h = 0
        self.f = 0
        self.circle = None
        self.neighbors = []
        self.parent = None
        self.wall = False
        if random.random() < 0.4 and not (self.x == SpotCircle.cols - 1 and self.y == SpotCircle.rows - 1):
            self.wall = True

        # print(str(self.x) + " " + str(self.y) + "   " + str(self.height) + " " + str(self.width))

    def show(self):
        # print("x: " + str(self.x * self.width) + " to " + str(self.x * self.width + self.width) + "  y: " + str(
        # self.y * self.height) + " to " + str(self.y * self.height + self.height))

        color = "white"
        outline = ""
        if self.wall:
            color = "black"
            outline = 'black'
        self.circle = SpotCircle.c.create_oval(self.x * SpotCircle.width, self.y * SpotCircle.height,
                                               self.x * SpotCircle.width + SpotCircle.width,
                                               self.y * SpotCircle.height + SpotCircle.height,
                                               fill=color, outline=outline)

    def print(self, text):
        SpotCircle.c.create_text(self.x * SpotCircle.width + SpotCircle.width / 2,
                                 self.y * SpotCircle.height + SpotCircle.height / 2,
                                 text=text)

    def printCoordinates(self):
        return str(self.y) + " " + str(self.x)

    def addNeighbors(self):
        col = self.x
        row = self.y

        if col < SpotCircle.cols - 1:
            self.neighbors.append(SpotCircle.grid[row][col + 1])
        if col > 0:
            self.neighbors.append(SpotCircle.grid[row][col - 1])
        if row < SpotCircle.rows - 1:
            self.neighbors.append(SpotCircle.grid[row + 1][col])
        if row > 0:
            self.neighbors.append(SpotCircle.grid[row - 1][col])

        # Diagonals
        if row > 0 and col > 0:
            self.neighbors.append(SpotCircle.grid[row - 1][col - 1])

        if row > 0 and col < SpotCircle.cols - 1:
            self.neighbors.append(SpotCircle.grid[row - 1][col + 1])

        if row < SpotCircle.rows - 1 and col < SpotCircle.cols - 1:
            self.neighbors.append(SpotCircle.grid[row + 1][col + 1])

        if row < SpotCircle.rows - 1 and col > 0:
            self.neighbors.append(SpotCircle.grid[row + 1][col - 1])
