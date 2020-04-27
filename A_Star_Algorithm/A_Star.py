rows = 3
cols = 5

grid = [[0] * cols] * rows

def spot():
    f = 0
    g = 0
    h = 0

for row in range(len(grid)):
    for col in range(len(grid[row])):
        grid[row][col] = spot()
        print(grid[row][col])





