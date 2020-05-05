from Spot import Spot
from tkinter import *
import math
import time

root = Tk()
c = Canvas(root, height=600, width=600, bg="white")
Spot.c = c

rows = 50
cols = 50
grid = []
Spot.rows = rows
Spot.cols = cols

squareHeight = int(c.cget("height")) / rows
squareWidth = int(c.cget("width")) / cols
Spot.height = squareHeight
Spot.width = squareWidth

openSet = []
closedSet = []
lowestF = 0
current = None
neighbors = None
tempG = 0

temp = None
done = False

newPath = False


def createCanvas():
    root.geometry('600x600')
    c.pack()


def createSpotGrid():
    for row in range(rows):
        grid.append([])

    for row in range(rows):
        for col in range(cols):
            grid[row].append(cols)

    for row in range(rows):
        for col in range(cols):
            grid[row][col] = Spot(row, col)

    Spot.grid = grid

    for row in range(rows):
        for col in range(cols):
            grid[row][col].addNeighbors()

    for row in range(rows):
        for col in range(cols):
            grid[row][col].show()


def heuristic(neighbor, end):
    distance = math.dist([neighbor.y, neighbor.x], [end.y, end.x])
    # distance = abs(end.x - neighbor.x) + abs(end.y - neighbor.y)
    return distance


def track():
    path = []
    temp = current
    path.append(temp)
    while temp.parent is not None:
        path.append(temp.parent)
        temp = temp.parent

    for spot in path:
        c.itemconfig(spot.square, fill="blue")


createCanvas()
createSpotGrid()

start = grid[0][0]
end = grid[rows - 1][cols - 1]
openSet.append(start)

while len(openSet) > 0 and not done:

    lowestF = 0

    for index in range(len(openSet)):
        if openSet[index].f < openSet[lowestF].f:
            lowestF = index

    current = openSet[lowestF]
    # current.print(c, "T")

    if current == end:
        print("Done")
        done = True
        break

    openSet.remove(current)
    closedSet.append(current)

    neighbors = current.neighbors

    for neighbor in neighbors:
        # neighbor.print(c, "n")
        if not closedSet.count(neighbor) > 0 and not neighbor.wall:
            tempG = current.g + 1
            newPath = False

            if openSet.count(neighbor) > 0:
                if tempG < neighbor.g:
                    neighbor.g = tempG
                    newPath = True

            else:
                neighbor.g = tempG
                openSet.append(neighbor)
                newPath = True

            if newPath:
                neighbor.h = heuristic(neighbor, end)
                neighbor.f = neighbor.g + neighbor.h
                # neighbor.print(str(neighbor.h) + " " + str(neighbor.g) )
                neighbor.parent = current
                # time.sleep(0.2)

    for spot in openSet:
        c.itemconfig(spot.square, fill="green")

    for spot in closedSet:
        c.itemconfig(spot.square, fill="red")

    track()

    root.update_idletasks()
    root.update()

if done:
    track()
else:
    print("No solution")
    for spot in grid:
        c.itemconfig(spot.square, fill="red")

mainloop()
