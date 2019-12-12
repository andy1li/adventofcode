# https://adventofcode.com/2018/day/10

from itertools import count
from typing import NamedTuple
import re

class Star(NamedTuple):
    x : int; y : int
    vx: int; vy: int

    def step(self):
        x, y, vx, vy = self 
        return Star(x+vx, y+vy, vx, vy)

def parse_stars(input):
    PATTERN = 'position=<(.+), (.+)> velocity=<(.+), (.+)>'
    return [
        Star(*map(int, re.match(PATTERN, line).groups()))
        for line in input
    ]

def visualize(stars, MAGIC):
    min_x = min(s.x for s in stars)
    min_y = min(s.y for s in stars)
    max_x = max(s.x for s in stars)
    max_y = max(s.y for s in stars)

    if max(max_x-min_x, max_y-min_y) <= MAGIC:
        print() # print(min_x, min_y, max_x, max_y)
        xys = set((x, y) for x, y, _, _ in stars)
        for y in range(min_y, max_y+1):
            for x in range(min_x, max_x+1):
                print('*' if (x, y) in xys else ' ', end='')
            print()
        return True

def both_stars(stars, MAGIC=62):
    for i in count():
        if visualize(stars, MAGIC): return i
        stars = [star.step() for star in stars]

TEST = '''position=< 9,  1> velocity=< 0,  2>
position=< 7,  0> velocity=<-1,  0>
position=< 3, -2> velocity=<-1,  1>
position=< 6, 10> velocity=<-2, -1>
position=< 2, -4> velocity=< 2,  2>
position=<-6, 10> velocity=< 2, -2>
position=< 1,  8> velocity=< 1, -1>
position=< 1,  7> velocity=< 1,  0>
position=<-3, 11> velocity=< 1, -2>
position=< 7,  6> velocity=<-1, -1>
position=<-2,  3> velocity=< 1,  0>
position=<-4,  3> velocity=< 2,  0>
position=<10, -3> velocity=<-1,  1>
position=< 5, 11> velocity=< 1, -2>
position=< 4,  7> velocity=< 0, -1>
position=< 8, -2> velocity=< 0,  1>
position=<15,  0> velocity=<-2,  0>
position=< 1,  6> velocity=< 1,  0>
position=< 8,  9> velocity=< 0, -1>
position=< 3,  3> velocity=<-1,  1>
position=< 0,  5> velocity=< 0, -1>
position=<-2,  2> velocity=< 2,  0>
position=< 5, -2> velocity=< 1,  2>
position=< 1,  4> velocity=< 2,  1>
position=<-2,  7> velocity=< 2, -2>
position=< 3,  6> velocity=<-1, -1>
position=< 5,  0> velocity=< 1,  0>
position=<-6,  0> velocity=< 2,  0>
position=< 5,  9> velocity=< 1, -2>
position=<14,  7> velocity=<-2,  0>
position=<-3,  6> velocity=< 2, -1>'''.split('\n')
    
if __name__ == '__main__':
    assert both_stars(parse_stars(TEST), 10) == 3
    print(both_stars(parse_stars(open('data/day10.in'))))