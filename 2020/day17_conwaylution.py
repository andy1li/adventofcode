# https://adventofcode.com/2020/day/17
# Originally from @thomasahle https://www.reddit.com/r/adventofcode/comments/keqsfa/2020_day_17_solutions/gg4kafh/

import numpy as np
from scipy.ndimage import convolve

def boot(raw, ndim):
    grid = [[x=="#" for x in line.strip()] for line in raw]
    grid = np.expand_dims(grid, axis=tuple(range(ndim-2)))
    neighbors = np.ones(tuple([3] * ndim))
    neighbors[tuple([1] * ndim)] = 0

    for _ in range(6):  
        grid = np.pad(grid, 1).astype(int)
        cnt = convolve(grid, neighbors, mode="constant")
        grid = (cnt == 3) | (grid & (cnt == 2))
    return grid.sum()

TEST = '''\
.#.
..#
###'''.splitlines()

if __name__ == '__main__':
    assert boot(TEST, 3) == 112
    assert boot(TEST, 4) == 848
    raw = open('data/day17.in').readlines()
    print(boot(raw, 3))
    print(boot(raw, 4))