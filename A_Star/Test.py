rows = 3
cols = 9

grid = []

for row in range(rows):
    grid.append([])

for row in range(rows):
    for col in range(cols):
        grid[row].append(col)

for row in range(rows):
    for col in range(cols):
        grid[row][col] = str(col) + str(row)

for row in grid:
    print(row)




