# https://adventofcode.com/2019/day/12

from itertools import combinations, count
from functools import reduce
from numpy     import lcm
from typing    import NamedTuple
import re

class Moon:
    def __init__(self, line):
        PATTERN = '<x=(.+), y=(.+), z=(.+)>'
        self.x, self.y, self.z = map(int, re.match(PATTERN, line).groups())
        self.vx = self.vy = self.vz = 0

    def __repr__(self):
        return f'Moon[({self.x}, {self.y}, {self.z}), ({self.vx}, {self.vy}, {self.vz})]'

    def interact(self, other):    
        cmp = lambda a, b: (a > b) - (a < b)
        self.vx  += cmp(other.x, self.x)
        self.vy  += cmp(other.y, self.y)
        self.vz  += cmp(other.z, self.z)
        other.vx -= cmp(other.x, self.x)
        other.vy -= cmp(other.y, self.y)
        other.vz -= cmp(other.z, self.z)

    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz

    @property
    def energy(self):
        return (abs(self.x)+abs(self.y)+abs(self.z)) * (abs(self.vx)+abs(self.vy)+abs(self.vz))

def parse(input): return [*map(Moon, input)]

def step(moons):
    for a, b in combinations(moons, 2): a.interact(b)
    for m in moons: m.step()

def fst_star(moons, steps):
    # print(*moons, sep='\n') 
    for _ in range(steps): step(moons)
    return sum(m.energy for m in moons)

def snd_star(moons): 
    seen, cycles = [set(), set(), set()], [0, 0, 0]
    for i in count():
        sigs =  [
            tuple((m.x, m.vx) for m in moons),
            tuple((m.y, m.vy) for m in moons),
            tuple((m.z, m.vz) for m in moons)
        ]
        for j in range(3):
            if sigs[j] in seen[j] and not cycles[j]: cycles[j] = i
            seen[j].add(sigs[j])
        step(moons)
        
        if all(cycles): return reduce(lcm, cycles)

TEST1 = '''<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>'''.splitlines()
TEST2 = '''<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>'''.splitlines()

if __name__ == '__main__':
    assert fst_star(parse(TEST1), 10) == 179
    assert fst_star(parse(TEST2), 100) == 1940

    assert snd_star(parse(TEST1)) == 2772
    assert snd_star(parse(TEST2)) == 4686774924

    print(fst_star(parse(open('data/day12.in')), 1000))
    print(snd_star(parse(open('data/day12.in'))))