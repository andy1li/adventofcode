def get_neighbors(y, x):
    return [(y-1, x), (y, x+1), (y+1, x), (y, x-1)]

def iterate(grid):
    for y, row in enumerate(grid):
        for x, value in enumerate(row):
             yield y, x, value

def within_bounds(grid, y, x):
    height, width = len(grid), len(grid[0])
    return 0 <= y < height and 0 <= x < width