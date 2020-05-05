from SpotCircle import SpotCircle
from tkinter import *
import math
import time

root = Tk()
c = Canvas(root, height=600, width=600, bg="white")
SpotCircle.c = c

rows = 50
cols = 50
grid = []
SpotCircle.rows = rows
SpotCircle.cols = cols

circleHeight = int(c.cget("height")) / rows
circleWidth = int(c.cget("width")) / cols
SpotCircle.height = circleHeight
SpotCircle.width = circleWidth

openSet = []
closedSet = []
lowestF = 0
current = None
neighbors = None
tempG = 0

temp = None
done = False

newPath = False
line = 0


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
            grid[row][col] = SpotCircle(row, col)

    SpotCircle.grid = grid

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
    path.append(temp.x * circleWidth + circleWidth / 2)
    path.append(temp.y * circleHeight + circleHeight / 2)
    while temp.parent is not None:
        path.append(temp.parent.x * circleWidth + circleWidth / 2)
        path.append(temp.parent.y * circleHeight + circleHeight / 2)
        temp = temp.parent

        c.coords(line, path)



createCanvas()
createSpotGrid()

line = c.create_line(0, 0, 0, 0, width=circleWidth / 2, fill="blue")

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

    track()

    root.update_idletasks()
    root.update()

if done:
    track()
else:
    print("No solution")
    for rows in grid:
        for spot in rows:
            c.itemconfig(spot.circle, fill="red")

mainloop()
