from Spot import Spot
from tkinter import *

rows = 5
cols = 5
grid = [[None] * cols] * rows

openSet = []
closedSet = []

for row in range(len(grid)):
    for col in range(len(grid[row])):
        grid[row][col] = Spot(row, col)

start = grid[0][0]
end = grid[cols - 1][rows - 1]

openSet.append(start)

root = Tk()
root.geometry('400x400')
c = Canvas(root, height=400, width=400, bg="white")
c.pack()


for row in range(len(grid)):
    for col in range(len(grid[row])):
        grid[row][col].show(c, int(c.cget("height")) / rows, int(c.cget("width")) / cols, row, col)

root.mainloop()
