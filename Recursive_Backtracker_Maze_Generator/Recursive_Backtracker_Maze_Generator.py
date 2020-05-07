from Cell import Cell
from tkinter import *

rows = 10
cols = 10

Cell.rows = rows
Cell.cols = cols

root = Tk()
root.geometry('600x600')
c = Canvas(root, height=600, width=600, bg="black")
Cell.c = c
c.pack()

squareHeight = int(c.cget("height"))
squareWidth = int(c.cget("width"))
Cell.height = squareHeight
Cell.width = squareWidth

grid = []


def createGrid():
    for row in range(rows):
        for col in range(cols):
            grid.append(Cell(row, col))


createGrid()

for cell in grid:
    cell.show()

root.mainloop()
