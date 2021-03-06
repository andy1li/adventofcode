# https://adventofcode.com/2020/day/17

from collections import Counter
from itertools import product

def parse(raw, ndim):
    padding = (0,) * (ndim - 2)
    return { (x, y) + padding
        for y, row in enumerate(raw)
        for x, val in enumerate(row)
        if val == '#'
    }

def step(actives):
    neighbors = (
        tuple(map(sum, zip(point, delta)))
        for point in actives
        for delta in product([-1, 0, 1], repeat=len(point))
        if any(delta)
    )
    return { point
        for point, cnt in Counter(neighbors).items()
        if cnt == 3 or (point in actives and cnt == 2) 
    }

def boot(actives): 
    for i in range(6): actives = step(actives)
    return len(actives) 

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
