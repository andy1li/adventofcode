# https://adventofcode.com/2021/day/11

from advent import eight_neighbors as eight, neighbor_items, iterate
from itertools import count
from copy import deepcopy
import numpy as np

def parse(raw):
    return np.array([
        np.array(list(map(int, row.strip()))) 
        for row in raw
    ])

def step(grid):
    grid += 1

    bfs = [(y, x) for y, x, val in iterate(grid) if val > 9]
    for y, x in bfs:
        for (ny, nx), nval in neighbor_items(grid, y, x, eight):
            if nval == 9: bfs += (ny, nx),
            grid[ny][nx] += 1

    flashes = (grid > 9).sum()
    grid = np.where(grid > 9, 0, grid)
    return grid, flashes

def fst_star(grid, n=100):
    ans, grid = 0, deepcopy(grid)
    for _ in range(n):
        grid, flashes = step(grid)
        ans += flashes
    return ans

def snd_star(grid):
    for i in count(1):
        grid, flashes = step(grid)
        if np.all(grid == 0): return i

TEST = '''\
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526'''.splitlines()

if __name__ == '__main__':
    assert fst_star(parse(TEST)) == 1656
    assert snd_star(parse(TEST)) == 195

    grid = parse(open('data/day11.in'))
    print(fst_star(grid))
    print(snd_star(grid))