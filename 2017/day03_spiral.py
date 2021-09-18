# https://adventofcode.com/2017/day/3

from collections import defaultdict
from itertools import count

def spiral():
    i = 1; yield 1, 0 # i, pos
    for side_len in count(3, step=2):
        pos = (1 - 1j) * (side_len//2)
        dpos = 1j
        for _ in range(4):
            for _ in range(side_len-1):
                i += 1; pos += dpos
                yield i, pos
            dpos *= 1j

def fst_star(stop):
    abs_int = lambda x: abs(int(x))
    for x, pos in spiral():
        if x == stop: 
            return sum(map(abs_int, [pos.real, pos.imag]))

def snd_star(stop):
    grid = defaultdict(int, {0: 1})
    for i, pos in spiral():
        if i == 1: continue
        grid[pos] = sum( 
            grid[pos+dpos] 
            for dpos in [
                -1+1j,  1j, 1+1j, 
                -1   ,      1, 
                -1-1j, -1j, 1-1j, 
            ]
        )
        if grid[pos] > stop: return grid[pos]

if __name__ == '__main__':
    assert fst_star(1) == 0
    assert fst_star(12) == 3
    assert fst_star(23) == 2
    assert fst_star(1024) == 31

    print(fst_star(265149))
    print(snd_star(265149))

