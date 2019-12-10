# https://adventofcode.com/2019/day/10

from collections import defaultdict, deque
from math import atan2
from typing import NamedTuple

class Asteroid(NamedTuple): 
    x : int; y : int
        
def parse(input):
    return [ Asteroid(x, y)
        for y, row in enumerate(input)
        for x, val in enumerate(row)
        if val == '#'
    ]

def get_angles(asteroids, a):
    angles = defaultdict(set)
    for b in asteroids:
        if a == b: continue
        y, x = b.y-a.y, b.x-a.x
        angle = atan2(-x, y) # angle = atan2(y, x)
        angles[angle].add(b)
    return angles

def iter_(angles):
    while angles:
        if angles[0]: 
            yield angles[0].pop()
            angles.rotate(-1)
        else:
            angles.popleft()

def fst_star(asteroids): 
    return max( 
        (len(get_angles(asteroids, a)), a) 
        for a in asteroids 
    )

def snd_star(asteroids, best):
    manhattan = lambda other: -abs(best.x-other.x) - abs(best.y-other.y)

    angles = get_angles(asteroids, best)
    angles = deque( 
        sorted(angles[a], key=manhattan)
        for a in sorted(angles)
    )
    angles.rotate(1)
    asteroids = iter_(angles)

    for _ in range(200): asteroid = next(asteroids)
    return asteroid.x * 100 + asteroid.y

    
TEST1 = '''.#..#
.....
#####
....#
...##'''.split('\n')
TEST2 = '''.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##'''.split('\n')

if __name__ == '__main__':
    assert fst_star(parse(TEST1))[0] == 8

    asteroids = parse(TEST2)
    num, best = fst_star(asteroids); assert num == 210
    assert snd_star(asteroids, best) == 802

    asteroids = parse(open('data/day10.in'))
    num, best = fst_star(asteroids); print(num)
    print(snd_star(asteroids, best))