# https://adventofcode.com/2020/day/11

from advent import *
from itertools import chain

def count_occupied(xs):
    return sum(x=='#' for x in xs)

def step(grid, get_nbrs, tolerance):
    m, n = len(grid), len(grid[0])
    new_grid = [list('.' * n) for _ in range(m)]
    for y, x, val in iterate(grid):
        if val == '.': continue
        cnt = count_occupied(get_nbrs(grid, y, x))
        if val == 'L' and cnt == 0: new_grid[y][x] = '#'
        elif val == '#' and cnt >= tolerance: new_grid[y][x] = 'L'
        else: new_grid[y][x] = grid[y][x]
    return new_grid

def immediate_nbrs(grid, y, x):
    yield from (v for _, v in get_neighbor_items(grid, y, x))

def visible_nbrs(grid, y, x):
    def seat(dydx, ny=y, nx=x):
        dy, dx = dydx
        while within_bounds(grid, ny+dy, nx+dx):
            ny, nx = ny+dy, nx+dx
            if grid[ny][nx] != '.': 
                return grid[ny][nx]
    yield from map(seat, eight_neighbors)

def equilibrium(grid, count_nbrs, tolerance=4): 
    prev = None
    while grid != prev:
        grid, prev = step(grid, count_nbrs, tolerance), grid
    return count_occupied(chain(*grid))

TEST = [*map(list, '''\
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL'''.splitlines())]

if __name__ == '__main__':
    assert equilibrium(TEST, immediate_nbrs) == 37
    assert equilibrium(TEST, visible_nbrs, 5) == 26
    grid = [list(row.strip()) for row in open('data/day11.in')]
    print(equilibrium(grid, immediate_nbrs))
    print(equilibrium(grid, visible_nbrs, 5))
    