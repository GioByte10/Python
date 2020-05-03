from Spot import Spot
from tkinter import *

root = Tk()
c = Canvas(root, height=400, width=400, bg="white")

rows = 10
cols = 10
grid = []

squareHeight = int(c.cget("height")) / rows
squareWidth = int(c.cget("width")) / cols

openSet = []
closedSet = []


def createCanvas():
    root.geometry('400x400')
    c.pack()


def createSpotGrid():
    for row in range(rows):
        grid.append([])

    for row in range(rows):
        for col in range(cols):
            grid[row].append(cols)

    for row in range(rows):
        for col in range(cols):
            print(str(squareHeight) + " " + str(squareWidth))
            grid[row][col] = Spot(row, col, squareHeight, squareWidth)

    for row in range(rows):
        for col in range(cols):
            grid[row][col].show(c, "white")


createCanvas()
createSpotGrid()

start = grid[0][0]
end = grid[rows - 1][cols - 1]
openSet.append(start)

while len(openSet) > 0:
    for spot in openSet:
        spot.show(c, "green")

    root.update_idletasks()
    root.update()
