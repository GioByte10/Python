import random


class SpotSquare:
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
        self.square = None
        self.neighbors = []
        self.parent = None
        self.wall = False
        if random.random() < 0.4 and not (self.x == SpotSquare.cols - 1 and self.y == SpotSquare.rows - 1):
            self.wall = True

        # print(str(self.x) + " " + str(self.y) + "   " + str(self.height) + " " + str(self.width))

    def show(self):
        # print("x: " + str(self.x * self.width) + " to " + str(self.x * self.width + self.width) + "  y: " + str(
        # self.y * self.height) + " to " + str(self.y * self.height + self.height))

        color = "white"
        if self.wall:
            color = "black"
        self.square = SpotSquare.c.create_rectangle(self.x * SpotSquare.width, self.y * SpotSquare.height,
                                                    self.x * SpotSquare.width + SpotSquare.width,
                                                    self.y * SpotSquare.height + SpotSquare.height, fill=color)

    def print(self, text):
        SpotSquare.c.create_text(self.x * SpotSquare.width + SpotSquare.width / 2,
                                 self.y * SpotSquare.height + SpotSquare.height / 2,
                                 text=text)

    def printCoordinates(self):
        return str(self.y) + " " + str(self.x)

    def addNeighbors(self):
        col = self.x
        row = self.y

        if col < SpotSquare.cols - 1:
            self.neighbors.append(SpotSquare.grid[row][col + 1])
        if col > 0:
            self.neighbors.append(SpotSquare.grid[row][col - 1])
        if row < SpotSquare.rows - 1:
            self.neighbors.append(SpotSquare.grid[row + 1][col])
        if row > 0:
            self.neighbors.append(SpotSquare.grid[row - 1][col])

        if row > 0 and col > 0:
            self.neighbors.append(SpotSquare.grid[row - 1][col - 1])

        if row > 0 and col < SpotSquare.cols - 1:
            self.neighbors.append(SpotSquare.grid[row - 1][col + 1])

        if row < SpotSquare.rows - 1 and col < SpotSquare.cols - 1:
            self.neighbors.append(SpotSquare.grid[row + 1][col + 1])

        if row < SpotSquare.rows - 1 and col > 0:
            self.neighbors.append(SpotSquare.grid[row + 1][col - 1])
