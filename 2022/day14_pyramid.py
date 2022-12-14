# https://adventofcode.com/2022/day/14

from itertools import chain, count, product
from typing import NamedTuple

class Bounds(NamedTuple):
    min_x: int; min_y: int
    max_x: int; max_y: int

def parse_pair(pair):
    a, b = pair
    lo_x, hi_x = sorted([a[0], b[0]])
    lo_y, hi_y = sorted([a[1], b[1]])
    return product(range(lo_x, hi_x+1), range(lo_y, hi_y+1))

def parse_line(line):
    xys = [list(map(int, xy.split(','))) for xy in line.split('->')]
    pairs = zip(xys, xys[1:])
    yield from chain.from_iterable(map(parse_pair, pairs))

def parse(raw):
    rocks = set()
    min_x, min_y = [ float('inf')] * 2
    max_x, max_y = [-float('inf')] * 2
    for x, y in chain.from_iterable(map(parse_line, raw)):
        rocks.add((x, y))
        min_x = min(min_x, x); min_y = min(min_y, y)
        max_x = max(max_x, x); max_y = max(max_y, y)
    return rocks, Bounds(min_x, min_y, max_x, max_y)

def show():
    scan = [
        ['.' for x in range(bounds.min_x-1, bounds.max_x+2)]
        for y in range(bounds.min_y, bounds.max_y+1)
    ]
    for x, y in rocks: scan[y-bounds.min_y][x-bounds.min_x+1] = '#'
    for x, y in rests: scan[y-bounds.min_y][x-bounds.min_x+1] = 'o'
    for row in scan: print(''.join(row))
    print()

def is_empty(x, y):
    return ((x, y) not in rocks
        and (x, y) not in rests)

def fall(x=500, y=0):
    if y > bounds.max_y: 
        return (x, y) if correct else 'flow'
    if   is_empty(x,   y+1): return fall(x,   y+1)
    elif is_empty(x-1, y+1): return fall(x-1, y+1)
    elif is_empty(x+1, y+1): return fall(x+1, y+1)
    return x, y

def both_stars():
    for i in count():
        res = fall()
        if res in ['flow', (500, 0)]: return i
        rests.add(res)

TEST = '''\
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9'''.splitlines()

if __name__ == '__main__':
    rocks, bounds = parse(TEST)
    rests, correct = set(), False # type: ignore
    assert both_stars() == 24

    rocks, bounds = parse(TEST)
    rests, correct = set(), True # type: ignore
    assert both_stars() + 1 == 93

    rocks, bounds = parse(open('data/day14.in'))
    rests, correct = set(), False # type: ignore
    print(both_stars())

    rocks, bounds = parse(open('data/day14.in'))
    rests, correct = set(), True # type: ignore
    print(both_stars() + 1)