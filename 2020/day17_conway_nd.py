# https://adventofcode.com/2020/day/17

from collections import Counter
from itertools import product

def parse(raw, dimension):
    pad = (0,) * (dimension-2)
    return { (x, y) + pad
        for y, row in enumerate(raw)
        for x, val in enumerate(row)
        if val == '#'
    }

def step(grid):
    neighbors = (
        tuple(map(sum, zip(point, delta)))
        for point in grid
        for delta in product([-1, 0, 1], repeat=len(point))
        if any(delta)
    )
    return { point
        for point, cnt in Counter(neighbors).items()
        if cnt == 3 or (point in grid and cnt == 2) 
    }

def boot(grid): 
    for i in range(6): grid = step(grid)
    return len(grid) 

TEST = '''\
.#.
..#
###'''.splitlines()

if __name__ == '__main__':
    assert boot(parse(TEST, 3)) == 112
    assert boot(parse(TEST, 4)) == 848
    raw = open('data/day17.in').readlines()
    print(boot(parse(raw, 3)))
    print(boot(parse(raw, 4)))
