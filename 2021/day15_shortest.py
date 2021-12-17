# https://adventofcode.com/2021/day/15

from advent import iterate, neighbor_items
from networkx import DiGraph, shortest_path_length
from copy import deepcopy
import numpy as np

def increase_risk(grid, n):
    grid = deepcopy(grid) + n
    grid = np.where(grid <= 9, grid, grid-9)
    return grid

def augment(grid):
    grid = np.array([np.array(list(map(int, row))) for row in grid])
    grid = np.hstack([increase_risk(grid, i) for i in range(5)])
    grid = np.vstack([increase_risk(grid, i) for i in range(5)])
    return grid

def shortest(grid):
    G = DiGraph()
    for y, x, val in iterate(grid):
        for (ny, nx), nval in neighbor_items(grid, y, x):
            G.add_edge((y, x), (ny, nx), risk=int(nval))
    n, m = len(grid), len(grid[0])
    return shortest_path_length(G, (0, 0), (n-1, m-1), 'risk')

TEST = '''\
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581'''.splitlines()

if __name__ == '__main__':
    assert shortest(TEST) == 40
    assert  shortest(augment(TEST)) == 315

    grid = open('data/day15.in').read().splitlines()
    print(shortest(grid))
    print(shortest(augment(grid)))