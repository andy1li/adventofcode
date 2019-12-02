# https://adventofcode.com/2018/day/25

from typing import NamedTuple
from itertools import combinations

class Pos(NamedTuple):
    x: int; y: int; z: int; t: int

    def __sub__(a, b):
        return (abs(a.x-b.x) + abs(a.y-b.y) + abs(a.z-b.z) + abs(a.t-b.t))

class DisjointSets:
    def __init__(union):
        union.sets = {}

    def find(union, x):
        if union.sets[x] != x: 
            union.sets[x] = union.find(union.sets[x])
        return union.sets[x]

    def union(union, x, y):
        union.sets.setdefault(x, x)
        union.sets.setdefault(y, y)
        union.sets[union.find(y)] = union.find(x) 

    def all_sets(union):
        return set(map(union.find, union.sets))

def parse_line(line):
    return Pos(*map(int, line.split(',')))

def parse(input):
    cons, points = DisjointSets(), map(parse_line, input)
    for a, b in combinations(points, 2):
        if a - b <= 3: 
            cons.union(a, b)
        else:
            cons.union(a, a)
            cons.union(b, b)
    return cons

def fst_star(constellations): 
    return len(constellations.all_sets())

def snd_star(x):
    pass

TEST1 = ''' 0,0,0,0
 3,0,0,0
 0,3,0,0
 0,0,3,0
 0,0,0,3
 0,0,0,6
 9,0,0,0
12,0,0,0'''.split('\n')

TEST2 = '''-1,2,2,0
0,0,2,-2
0,0,0,-2
-1,2,0,0
-2,-2,-2,2
3,0,2,-1
-1,3,2,2
-1,0,-1,0
0,2,1,-2
3,0,0,0'''.split('\n')

TEST3 = '''1,-1,0,1
2,0,-1,0
3,2,-1,0
0,0,3,1
0,0,-1,-1
2,3,-2,0
-2,2,0,0
2,-2,0,-1
1,-1,0,-1
3,2,0,2'''.split('\n')

if __name__ == '__main__':
    assert fst_star(parse(TEST1)) == 2
    assert fst_star(parse(TEST2)) == 4
    assert fst_star(parse(TEST3)) == 3
    print(fst_star(parse(open('data/day25.in'))))
   