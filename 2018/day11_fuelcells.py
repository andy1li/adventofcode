# https://adventofcode.com/2018/day/11

from collections import defaultdict
from itertools import product
from tqdm import trange

def power(y, x, serial):
    rack_id = x + 10
    power = (rack_id*y + serial) * rack_id
    return (power//100)%10 - 5

def fst_star(serial):
    grid = {
        (y, x): power(y, x, serial)
        for y, x in product(range(1, 301), repeat=2)
    }
    yx = max(
        product(range(1, 299), repeat=2),
        key=lambda yx: sum(
            grid[iy, ix]
            for iy in range(yx[0], yx[0]+3)
            for ix in range(yx[1], yx[1]+3)
        )
    )
    return yx[1], yx[0]

def snd_star(serial):
    summed_area, max_p = [[0]*301 for _ in range(301)], 6
    
    for y, x in product(range(1, 301), repeat=2):
        p = power(y, x, serial)
        summed_area[x][y] = (
            - summed_area[y-1][x-1] + summed_area[y][x-1] 
            + summed_area[y-1][x]   + p
        )
        if p > max_p:
            max_p, max_y, max_x = p, y, x

    for d in trange(1, 300):
        for y, x in product(range(1, 301-d), repeat=2):
            p = (
                summed_area[y-1][x-1] - summed_area[y+d][x-1]
              - summed_area[y-1][x+d] + summed_area[y+d][x+d]
            )
            if p > max_p:
                max_p, max_y, max_x, max_s = p, y, x, d+1

    return max_x, max_y, max_s

if __name__ == '__main__':
    # assert power(3, 5, 8) == 4
    assert fst_star(18) == (33, 45)
    # assert fst_star(42) == (21, 61)
    # assert snd_star(18) == (90, 269, 16)
    # assert snd_star(42) == (232, 251, 12)

    print(fst_star(3463))
    print(snd_star(3463))