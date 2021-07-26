from Cell import Cell
from tkinter import *
import time

rows = 10
cols = 10

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
        grid.append([])

    for row in range(rows):
        for col in range(cols):
            grid[row].append(cols)

    for row in range(rows):
        for col in range(cols):
            grid[row][col] = (Cell(row, col))

    Cell.grid = grid

    for row in range(rows):
        for col in range(cols):
            grid[row][col].show()


def removeWalls(current, next):
    x = current.x - next.x
    y = current.y - next.y

    if x == -1:
        c.after(0, c.delete, current.right)
        c.after(0, c.delete, next.left)
        current.walls[1] = False
        next.walls[3] = False

    elif x == 1:
        c.after(0, c.delete, current.left)
        c.after(0, c.delete, next.right)
        current.walls[3] = False
        next.walls[1] = False

    if y == -1:
        c.after(0, c.delete, current.bottom)
        c.after(0, c.delete, next.top)
        current.walls[2] = False
        next.walls[0] = False

    elif y == 1:
        c.after(0, c.delete, current.top)
        c.after(0, c.delete, next.bottom)
        current.walls[0] = False
        next.walls[2] = False


createCanvas()
createGrid()

current = grid[0][0]
current.visited = True
current.changeColor()

while True:

    current.visited = True
    next = current.getNeighbor()

    if next is not None:
        stack.append(current)
        removeWalls(current, next)

        for cell in stack:
            cell.show()

        current = next

    elif len(stack) > 0:
        current = stack.pop()

    else:
        break

    root.update_idletasks()
    root.update()

    # time.sleep(0.1)

root.mainloop()


