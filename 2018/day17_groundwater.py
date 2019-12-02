# https://adventofcode.com/2018/day/17

from itertools import product, chain
from typing import NamedTuple
from sys import setrecursionlimit
setrecursionlimit(10**9)

class Bounds(NamedTuple):
    min_x: int; min_y: int
    max_x: int; max_y: int

def parse_line(line):
    xy = {}
    single, multiple = line.split(', ')

    ax, num = single.split('=')
    xy[ax] = [int(num)]

    ax, lohi = multiple.split('=')
    lo, hi = map(int, lohi.split('..'))
    xy[ax] = range(lo, hi+1)

    return product(xy['y'], xy['x'])

def parse(input):
    clays = set()
    min_x, min_y = [float('inf')] * 2
    max_x, max_y = [-float('inf')] * 2
    for y, x in chain.from_iterable(map(parse_line, input)):
        clays.add((y, x))
        min_x = min(min_x, x); min_y = min(min_y, y)
        max_x = max(max_x, x); max_y = max(max_y, y)
    return clays, Bounds(min_x, min_y, max_x, max_y)

def is_empty(y, x):
    return ((y, x) not in clays
        and (y, x) not in flows
        and (y, x) not in rests)

def is_solid(y, x):
    return ((y, x) in clays 
         or (y, x) in rests)

def horizontal(y, x):
    lo = x - 1
    while ((y, lo) not in clays
    and is_solid(y+1, lo+1)): lo -= 1

    hi = x + 1
    while ((y, hi) not in clays
    and is_solid(y+1, hi-1)): hi += 1

    if set([(y, lo), (y, hi)]).issubset(clays):
        for x in range(lo+1, hi):
            flows.discard((y, x)) 
            rests.add((y, x))
    else:
        for x in range(lo+1, hi):
            if (y, x) in rests: continue
            flows.add((y, x))
            if is_empty(y+1, x): fall(y, x)
            
def fall(y, x):
    if y <= bounds.max_y:
        flows.add((y, x))
        if is_empty(y+1, x): fall(y+1, x)
        if is_solid(y+1, x): horizontal(y, x)

def show():
    scan = [
        ['.' for x in range(bounds.min_x-1, bounds.max_x+2)]
        for y in range(bounds.min_y, bounds.max_y+1)
    ]
    for y, x in clays: scan[y-bounds.min_y][x-bounds.min_x+1] = '#'
    for y, x in flows: scan[y-bounds.min_y][x-bounds.min_x+1] = '|'
    for y, x in rests: scan[y-bounds.min_y][x-bounds.min_x+1] = '~'

    for row in scan: print(''.join(row))
    print()

def both_stars():
    fall(bounds.min_y, 500)
    show()
    return len(flows|rests), len(rests)

TEST = '''x=495, y=2..7
y=7, x=495..501
x=501, y=3..7
x=498, y=2..4
x=506, y=1..2
x=498, y=10..13
x=504, y=10..13
y=13, x=498..504'''.split('\n')

if __name__ == '__main__':
    clays, bounds = parse(TEST)
    flows, rests = set(), set()
    assert both_stars() == (57, 29)

    clays, bounds = parse(open('data/day17.in'))
    flows, rests = set(), set()
    print(both_stars())