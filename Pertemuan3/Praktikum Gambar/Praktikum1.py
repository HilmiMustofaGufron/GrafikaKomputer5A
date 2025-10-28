rows, cols = 10, 10
grid = [['.' for _ in range(cols)] for _ in range(rows)]

grid[4-1][6-1] = 'X'

for row in grid:
    print(''.join(row))
