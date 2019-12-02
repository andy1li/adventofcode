# https://adventofcode.com/2018/day/6

from collections import Counter, defaultdict
from itertools import chain, repeat
from typing import NamedTuple

class Point(NamedTuple): x: int; y: int

def parse(input): return [
    Point(*map(int, line.split(', '))) 
    for line in input
]

def get_bounds(points):
    min_x = min(p.x for p in points)
    min_y = min(p.y for p in points)
    max_x = max(p.x for p in points)
    max_y = max(p.y for p in points)
    return min_x, min_y, max_x, max_y

def closest(points, x, y):
    by_dist = defaultdict(set)
    for i, p in enumerate(points):
        if p == (x, y): return i
        distance = abs(p.x-x) + abs(p.y-y)
        by_dist[distance].add(i)

    close = by_dist[min(by_dist)]
    if len(close) == 1: return close.pop()
    else              : return '.'

def visualize(min_x, min_y, max_x, max_y, space):
    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            print(space[x, y], end='')
        print()

def fst_star(points):
    min_x, min_y, max_x, max_y = get_bounds(points)
    space = {
        (x, y): closest(points, x, y)
        for x in range(min_x, max_x+1)
        for y in range(min_y, max_y+1)
    }
    # visualize(min_x, min_y, max_x, max_y, space)
    infs = set( space[x, y]
        for x, y in chain(
            zip(repeat(min_x), range(min_y, max_y+1)),
            zip(repeat(max_x), range(min_y, max_y+1)),
            zip(range(min_x, max_x+1), repeat(min_y)),
            zip(range(min_x, max_x+1), repeat(max_y))
        )
    )
    largest = Counter( idx
        for idx in space.values()
        if idx not in infs|set('.')
    ).most_common(1)
    return largest[0][1]

def snd_star(points, safe=10000):
    min_x, min_y, max_x, max_y = get_bounds(points)
    margin = safe // len(points)
    return sum(
        sum(abs(p.x-x) + abs(p.y-y) for p in points) < safe
        for x in range(min_x-margin, max_x+margin)
        for y in range(min_y-margin, max_y+margin)
    )

TEST = '''1, 1
1, 6
8, 3
3, 4
5, 5
8, 9'''.split('\n')

if __name__ == '__main__':
    assert fst_star(parse(TEST)) == 17
    assert snd_star(parse(TEST), 32) == 16

    points = parse(open('data/day06.in'))
    print(fst_star(points))
    print(snd_star(points))