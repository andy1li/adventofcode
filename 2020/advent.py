eight_neighbors = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), (+1, 0), ( 1, 1)
]

def get_neighbor_items(grid, y, x):
    for dy, dx in eight_neighbors:
        ny, nx = y+dy, x+dx
        if within_bounds(grid, ny, nx):
            yield (ny, nx), grid[ny][nx]

def iterate(grid):
    yield from (
        (y, x, val)
        for y, row in enumerate(grid)    
        for x, val in enumerate(row)
    )

def within_bounds(grid, y, x):
    height, width = len(grid), len(grid[0])
    return 0 <= y < height and 0 <= x < width