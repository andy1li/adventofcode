def iterate(grid):
    yield from (
        (y, x, val)
        for y, row in enumerate(grid)    
        for x, val in enumerate(row)
    )

