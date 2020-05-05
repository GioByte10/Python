import random


class Spot:

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
        if random.random() < 0.4 and not (self.x == Spot.cols - 1 and self.y == Spot.rows - 1):
            self.wall = True

        # print(str(self.x) + " " + str(self.y) + "   " + str(self.height) + " " + str(self.width))

    def show(self):
        # print("x: " + str(self.x * self.width) + " to " + str(self.x * self.width + self.width) + "  y: " + str(
        # self.y * self.height) + " to " + str(self.y * self.height + self.height))

        color = "white"
        if self.wall:
            color = "black"
        self.square = Spot.c.create_rectangle(self.x * Spot.width, self.y * Spot.height,
                                              self.x * Spot.width + Spot.width,
                                              self.y * Spot.height + Spot.height, fill=color)

    def print(self, text):
        Spot.c.create_text(self.x * Spot.width + Spot.width / 2, self.y * Spot.height + Spot.height / 2,
                           text=text)

    def printCoordinates(self):
        return str(self.y) + " " + str(self.x)

    def addNeighbors(self):
        col = self.x
        row = self.y

        if col < Spot.cols - 1:
            self.neighbors.append(Spot.grid[row][col + 1])
        if col > 0:
            self.neighbors.append(Spot.grid[row][col - 1])
        if row < Spot.rows - 1:
            self.neighbors.append(Spot.grid[row + 1][col])
        if row > 0:
            self.neighbors.append(Spot.grid[row - 1][col])

        if row > 0 and col > 0:
            self.neighbors.append(Spot.grid[row - 1][col - 1])

        if row > 0 and col < Spot.cols - 1:
            self.neighbors.append(Spot.grid[row - 1][col + 1])

        if row < Spot.rows - 1 and col < Spot.cols - 1:
            self.neighbors.append(Spot.grid[row + 1][col + 1])

        if row < Spot.rows - 1 and col > 0:
            self.neighbors.append(Spot.grid[row + 1][col - 1])
