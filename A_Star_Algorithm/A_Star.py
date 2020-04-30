from Spot import Spot
from _tkinter import*

rows = 5
cols = 5
grid = [[0] * cols] * rows

openSet = []
closedSet = []

for row in range(len(grid)):
    for col in range(len(grid[row])):
        grid[row][col] = Spot(row, col)
        print(grid[row][col])

start = grid[0][0];
end = grid[cols - 1][rows - 1]

openSet.append(start)