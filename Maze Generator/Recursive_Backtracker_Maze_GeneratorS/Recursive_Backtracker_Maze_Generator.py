from Cell import Cell
from tkinter import *
import time

rows = 7
cols = 7

Cell.rows = rows
Cell.cols = cols

root = Tk()
c = Canvas(root, height=600, width=600, bg="black")
Cell.c = c

squareHeight = int(c.cget("height")) / rows
squareWidth = int(c.cget("width")) / cols
Cell.height = squareHeight
Cell.width = squareWidth

grid = []
stack = []


def createCanvas():
    root.geometry('600x600+100-70')
    c.pack()


def createGrid():
    for row in range(rows):
        for col in range(cols):
            grid.append(Cell(row, col))

    Cell.grid = grid


def removeWalls(current, next):
    x = current.x - next.x
    y = current.y - next.y

    if x == -1:
        current.walls[1] = False
        next.walls[3] = False

    elif x == 1:
        current.walls[3] = False
        next.walls[1] = False

    if y == -1:
        current.walls[2] = False
        next.walls[0] = False

    elif y == 1:
        current.walls[0] = False
        next.walls[2] = False


createCanvas()
createGrid()

current = grid[0]

while True:

    for i in range(len(grid)):
        grid[i].show()

    current.visited = True
    current.highlight()

    next = current.getNeighbor()

    if next is not None:
        next.visited = True
        stack.append(current)
        removeWalls(current, next)

        current = next

    elif len(stack) > 0:
        current = stack.pop()

    else:
        break

    root.update_idletasks()
    root.update()

    # time.sleep(0.1)

root.mainloop()


