# https://adventofcode.com/2018/day/22

from advent import get_neighbor_items, iterate
from typing import NamedTuple
import networkx
import numpy as np

class Pos(NamedTuple): x: int; y: int

def scan_cave(depth, target, MOD=20183):
    y_times, x_times = 2, 3
    cave = np.zeros((target.y*y_times, target.x*x_times), dtype=int)
    cave[0,...] = (np.arange(target.x*x_times) * 16807 + depth) % MOD
    cave[...,0] = (np.arange(target.y*y_times) * 48271 + depth) % MOD

    for y in range(1, target.y*y_times):
        for x in range(1, target.x*x_times):
            cave[y, x] = ((cave[y, x-1] * cave[y-1, x]) + depth) % MOD

    cave[target.y, target.x] = depth
    return cave % 3

def fst_star(cave, target):
    return cave[:target.y+1,:target.x+1].sum()

def snd_star(cave, target):
    G = networkx.Graph()
    for y, x, val in iterate(cave):
        if val == 0: G.add_edge((y, x, 'gear'), (y, x, 'torch'), weight=7)
        if val == 1: G.add_edge((y, x, 'gear'), (y, x, 'neither'), weight=7)
        if val == 2: G.add_edge((y, x, 'torch'), (y, x, 'neither'), weight=7)

        for (ny, nx), nval in get_neighbor_items(cave, y, x):
            if val == 0 and nval == 0:
                G.add_edge((y, x, 'gear'), (ny, nx, 'gear'), weight=1)
                G.add_edge((y, x, 'torch'), (ny, nx, 'torch'), weight=1)
            if val == 0 and nval == 1:
                G.add_edge((y, x, 'gear'), (ny, nx, 'gear'), weight=1)
            if val == 0 and nval == 2:
                G.add_edge((y, x, 'torch'), (ny, nx, 'torch'), weight=1)

            if val == 1 and nval == 0:
                G.add_edge((y, x, 'gear'), (ny, nx, 'gear'), weight=1)
            if val == 1 and nval == 1:
                G.add_edge((y, x, 'gear'), (ny, nx, 'gear'), weight=1)
                G.add_edge((y, x, 'neither'), (ny, nx, 'neither'), weight=1)
            if val == 1 and nval == 2:
                G.add_edge((y, x, 'neither'), (ny, nx, 'neither'), weight=1)

            if val == 2 and nval == 0:
                G.add_edge((y, x, 'torch'), (ny, nx, 'torch'), weight=1)
            if val == 2 and nval == 1:
                G.add_edge((y, x, 'neither'), (ny, nx, 'neither'), weight=1)
            if val == 2 and nval == 2:
                G.add_edge((y, x, 'torch'), (ny, nx, 'torch'), weight=1)
                G.add_edge((y, x, 'neither'), (ny, nx, 'neither'), weight=1)

    return networkx.shortest_path_length(
        G, (0, 0, 'torch'), 
        (target.y, target.x, 'torch'), 
        weight='weight'
    )

if __name__ == '__main__':
    cave = scan_cave(510, Pos(10, 10))
    assert fst_star(cave, Pos(10, 10)) == 114
    assert snd_star(cave, Pos(10, 10)) == 45

    cave = scan_cave(10689, Pos(11, 722))
    print(fst_star(cave, Pos(11, 722)))
    print(snd_star(cave, Pos(11, 722)))