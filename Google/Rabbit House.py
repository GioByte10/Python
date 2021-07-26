def getHighest(grid, r, c):
    highest = [0, 0, 0]

    for row in range(r):
        for col in range(c):
            if grid[row][col] > highest[0]:
                highest = [grid[row][col], row, col]

    return highest


def addBoxes(r, c, grid, rMax, cMax, dif, searched):

    if not checkSearched(searched):

        neighbors = getNeighbors(r, c, grid, rMax, cMax)

        for neighbor in neighbors:
            if not searched[neighbor[1]][neighbor[2]]:
                if neighbor[0] - grid[r][c] > 1:
                    dif = neighbor[0] - grid[r][c] - 1
                    grid[r][c] += neighbor[0] - grid[r][c] - 1
                    searched[neighbor[1]][neighbor[2]] = True
                    return addBoxes(neighbor[1], neighbor[2], grid, rMax, cMax, dif, searched)



                elif grid[r][c] - neighbor[0] > 1:
                    dif = grid[r][c] - neighbor[0] - 1
                    grid[neighbor[1]][neighbor[2]] += grid[r][c] - neighbor[0] - 1
                    searched[neighbor[1]][neighbor[2]] = True
                    return addBoxes(neighbor[1], neighbor[2], grid, rMax, cMax, dif, searched)

    else:
        return dif


def getNeighbors(r, c, grid, rMax, cMax):
    neighbors = []

    if r + 1 < rMax:
        neighbors.append([grid[r + 1][c], r + 1, c])

    if r - 1 > - 1:
        neighbors.append([grid[r - 1][c], r - 1, c])

    if c + 1 < cMax:
        neighbors.append([grid[r][c + 1], r, c + 1])

    if c - 1 > cMax:
        neighbors.append([grid[r][c - 1], r, c - 1])

    return neighbors


def checkSearched(searched):
    for row in searched:
        for col in row:
            if not col:
                return False

    return True

import sys

T = int(sys.stdin.readline())

for i in range(1, T + 1):
    inputs = [int(x) for x in sys.stdin.readline().split()]

    rMax = inputs[0]
    cMax = inputs[1]

    grid = []
    searched = []
    sc = [False] * cMax

    for row in range(rMax):
        columns = [int(x) for x in sys.stdin.readline().split()]
        grid.append(columns)

    for row in range(rMax):
        searched.append([])

    for row in range(rMax):
        for col in range(cMax):
            searched[row].append(False)

    highest = getHighest(grid, rMax, cMax)
    n = highest[0]
    r = highest[1]
    c = highest[2]

    searched[r][c] = True

    result = addBoxes(r, c, grid, rMax, cMax, 0, searched)

    print("Case #" + str(i) + ": " + str(result))

