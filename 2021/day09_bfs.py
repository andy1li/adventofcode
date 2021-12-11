# https://adventofcode.com/2021/day/9

from advent import neighbor_items, iterate
from collections import Counter
from functools import reduce
from math import prod

def fst_star(grid): 
    return sum( 1 + int(val)
        for (y, x, val) in iterate(grid)
        if all( int(val) < int(nval)
            for (ny, nx), nval in neighbor_items(grid, y, x)
        )
    )

def snd_star(grid):
    bfs = [ (y, x, val, (y, x))   
        for (y, x, val) in iterate(grid)
        if all( int(val) < int(nval)
            for (ny, nx), nval in neighbor_items(grid, y, x)
        )
    ]
    seen = {}
    for (y, x, val, basin) in bfs:
        if (y, x) in seen: continue
        seen[y, x] = basin
        for (ny, nx), nval in neighbor_items(grid, y, x):
            if int(nval) > int(val) and int(nval) != 9:
                bfs.append( (ny, nx, nval, basin) )
    return prod( v
        for k, v in Counter(seen.values()).most_common(3)
    )

TEST = '''\
2199943210
3987894921
9856789892
8767896789
9899965678'''.splitlines()

if __name__ == '__main__':
    assert fst_star(TEST) == 15
    assert snd_star(TEST) == 1134

    grid = open('data/day09.in').read().splitlines()
    print(fst_star(grid))
    print(snd_star(grid))