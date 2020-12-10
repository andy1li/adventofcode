# https://adventofcode.com/2020/day/11

from advent import eight_neighbors, get_neighbor_items, iterate, within_bounds

def step(grid, count_nbrs, threshold):
    grid = [*map(list, grid)]
    m, n = len(grid), len(grid[0])
    new_grid = [list('.' * n) for _ in range(m)]
    for y, x, val in iterate(grid):
        if val == '.': continue
        cnt = count_nbrs(grid, y, x)
        if val == 'L' and cnt == 0: new_grid[y][x] = '#'
        elif val == '#' and cnt >= threshold: new_grid[y][x] = 'L'
        else: new_grid[y][x] = grid[y][x]
    return new_grid

def immediate_nbrs(grid, y, x): 
    return sum(v=='#' for _, v in get_neighbor_items(grid, y, x))

def visible_nbrs(grid, y, x):
    def is_occupied(dydx):
        (dy, dx), ny, nx = dydx, y, x
        while True:
            ny, nx = ny+dy, nx+dx
            if not within_bounds(grid, ny, nx): return False
            if grid[ny][nx] != '.': return grid[ny][nx] == '#'
    return sum(map(is_occupied, eight_neighbors()))

def equilibrium_occupied(grid, count_nbrs, threshold=4): 
    pre_grid = None
    while pre_grid != grid:
        grid, pre_grid = step(grid, count_nbrs, threshold), grid
    return sum(x=='#' for row in grid for x in row)

TEST = '''\
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL'''.splitlines()

if __name__ == '__main__':
    assert equilibrium_occupied(TEST, immediate_nbrs) == 37
    assert equilibrium_occupied(TEST, visible_nbrs, 5) == 26
    grid = [*map(str.strip, open('data/day11.in'))]
    print(equilibrium_occupied(grid, immediate_nbrs))
    print(equilibrium_occupied(grid, visible_nbrs, 5))
    