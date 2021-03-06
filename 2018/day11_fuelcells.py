# https://adventofcode.com/2018/day/11

from collections import defaultdict
from itertools import product

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
        summed_area[y][x] = (
            - summed_area[y-1][x-1] + summed_area[y][x-1] 
            + summed_area[y-1][x]   + p
        )
        if p > max_p:
            max_p, max_y, max_x = p, y, x

    for s in range(1, 300):
        for y, x in product(range(1, 301-s), repeat=2):
            p = (
                summed_area[y-1][x-1] - summed_area[y+s][x-1]
              - summed_area[y-1][x+s] + summed_area[y+s][x+s]
            )
            if p > max_p:
                max_p, max_y, max_x, max_s = p, y, x, s+1

    return max_x, max_y, max_s

if __name__ == '__main__':
    assert power(5, 3, 8) == 4
    assert fst_star(18) == (33, 45)
    assert fst_star(42) == (21, 61)
    # assert snd_star(18) == (90, 269, 16)
    # assert snd_star(42) == (232, 251, 12)

    print(fst_star(3463))
    print(snd_star(3463))