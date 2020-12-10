def eight_neighbors():
    return [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), (+1, 0), ( 1, 1)
    ]

def get_neighbor_items(grid, y, x):
    for dy, dx in eight_neighbors():
        ny, nx = y+dy, x+dx
        if within_bounds(grid, ny, nx):
            yield (ny, nx), grid[ny][nx]

def iterate(grid):
    for y, row in enumerate(grid):
        for x, value in enumerate(row):
             yield y, x, value

def within_bounds(grid, y, x):
    height, width = len(grid), len(grid[0])
    return 0 <= y < height and 0 <= x < width