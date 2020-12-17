# https://adventofcode.com/2020/day/17

from collections import defaultdict
from itertools import product

def parse(raw, dim):
    cube = defaultdict(bool)
    for y, row in enumerate(raw):
        for x, cell in enumerate(row.strip()):
            pos = (x, -y) + (0,) * (dim-2)
            cube[pos] = cell == '#'
    return cube

def iterate(cube):
    dim = len(list(cube)[0])
    mins = [float('inf')] * dim
    maxs = [-float('inf')] * dim
    for pos, i in product(cube, range(dim)):
        mins[i] = min(mins[i], pos[i])
        maxs[i] = max(maxs[i], pos[i])
    yield from product(
        *(range(mins[i]-1, maxs[i]+2) for i in range(dim))
    )

def get_neighbors(pos):
    dim = len(pos)
    for d_pos in product([-1, 0, 1], repeat=dim):
        if d_pos == (0,) * dim: continue
        yield tuple(pos[i] + d_pos[i] for i in range(dim))

def step(cube):
    new_cube = defaultdict(bool)
    for pos in iterate(cube):
        cnt = sum(cube[nbr] for nbr in get_neighbors(pos))
        new_cube[pos] = (
            (cube[pos] and 2 <= cnt <= 3) 
        or  (not cube[pos] and cnt == 3) 
        )
    return new_cube

def run(cube, show_progress=False, stop=6): 
    for i in range(stop):
        if show_progress: print(i+1, end=' ')
        cube = step(cube)
    return sum(cube.values()) 

TEST = '''\
.#.
..#
###'''.splitlines()

if __name__ == '__main__':
    assert run(parse(TEST, 3)) == 112
    # assert run(parse(TEST, 4), True) == 848
    cube = open('data/day17.in').readlines()
    print(run(parse(cube, 3)))
    print(run(parse(cube, 4), True))