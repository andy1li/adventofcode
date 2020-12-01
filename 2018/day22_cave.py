# https://adventofcode.com/2018/day/22

import numpy as np
from typing import NamedTuple

class Pos(NamedTuple): x: int; y: int

def scan_cave(depth, target, MOD=20183):
    cave = np.zeros((target.y+1, target.x+1), dtype=int)
    cave[0,...] = (np.arange(target.x+1) * 16807 + depth) % MOD
    cave[...,0] = (np.arange(target.y+1) * 48271 + depth) % MOD

    for y in range(1, target.y+1):
        for x in range(1, target.x+1):
            cave[y, x] = ((cave[y, x-1] * cave[y-1, x]) + depth) % MOD

    cave[target.y, target.x] = depth
    return cave % 3

def fst_star(depth, target): 
    return scan_cave(depth, target).sum()

def distance(tool, region): return 1 + (tool == region)

def snd_star():
    pass

if __name__ == '__main__':
    assert fst_star(510, Pos(10, 10)) == 114

    print(fst_star(10689, Pos(11, 722)))
    print(snd_star())