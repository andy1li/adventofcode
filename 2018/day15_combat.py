# https://adventofcode.com/2018/day/15

from bisect import bisect_left as bisect
from collections import deque
from copy import deepcopy
from itertools import count, filterfalse

class Creature:
    def __init__(self, y, x, race):
        self.pos = y, x
        self.race = race
        self.hp = 200
        self.power = 3

    def __repr__(self):
        return f"{'🧝‍♀️' if self.race=='E' else '👹'}@{self.pos} HP:{self.hp}"

    @property
    def is_dead(self): return self.hp <= 0

    @property
    def adjacent_enemies(self): 
        return set(adjacent(*self.pos)) & self.enemies

    def got_hit(self, injury):
        self.hp -= injury

    def bfs_next(self):
        q, p = deque([self.pos]), {} 
        while q:
            pos = q.popleft()
            if pos in self.target_sides:
                traceback = pos
                while p[traceback] != self.pos:
                    traceback = p[traceback]
                return traceback

            for next_pos in adjacent(*pos):
                if next_pos in self.disallow: continue
                self.disallow.add(next_pos)
                p[next_pos] = pos
                q.append(next_pos)

    def move(self, creatures):
        if self.adjacent_enemies: return
        
        self.target_sides = [
            (y, x)
            for pos in self.enemies
            for y, x in adjacent(*pos)
            if (y, x) not in self.disallow
        ]
        next_pos = self.bfs_next()
        if next_pos:
            self.pos = next_pos
            # print(' ➡️', self.pos)
     
    def attack(self, creatures):
        if not self.adjacent_enemies: return

        weakest = min([ c
                for c in creatures
                if c.pos in self.adjacent_enemies
            ],
            key=lambda c: (c.hp, c.pos)
        )
        weakest.got_hit(self.power)
        # print(' ⚔️', weakest.pos)

    def play_to_win(self, creatures):
        if self.is_dead: return 
        # print(self)
        self.disallow = set(self.walls)
        self.enemies = set()
        for i, c in enumerate(creatures):
            if c.is_dead: continue 
            self.disallow.add(c.pos)
            if c.race != self.race: 
                self.enemies.add(c.pos)

        if not self.enemies: return "Win!" 
        self.move(creatures)
        self.attack(creatures)

def parse(input):
    cave = [line.strip() for line in input]
    creatures, walls = [], set()
    for y, row in enumerate(cave):
        for x, cell in enumerate(row):
            if cell in 'EG': 
                creatures.append(Creature(y, x, cell))
                cave[y] = cave[y].replace(cell, '.', 1)
            if cell == '#':
                walls.add((y, x))
    for c in creatures:
        c.cave = cave
        c.walls = walls
    return creatures

def adjacent(y, x):
    return [(y-1, x), (y, x-1), (y, x+1), (y+1, x)]

def show(creatures):
    cave = creatures[0].cave[:]
    for c in creatures:
        y, x = c.pos
        cave[y] = cave[y][:x] + c.race + cave[y][x+1:]
    print(*cave, sep='\n', end='\n\n')

def fst_star(creatures, elf_power=3):
    creatures = deepcopy(creatures)
    num_elves = sum(c.race=='E' for c in creatures)
    for c in creatures:
        if c.race == 'E': c.power = elf_power
 
    for round in count():
        # print(f'\nRound {round}:')
        # show(creatures)
        creatures = sorted(
            filterfalse(lambda c: c.is_dead, creatures), 
            key=lambda c: c.pos
        )
        for creature in creatures:
            if creature.play_to_win(creatures):
                return (
                    round * sum( c.hp 
                        for c in creatures
                        if c.race == creature.race
                    ),
                    num_elves == sum(c.race=='E' for c in creatures)
                )

def snd_star(creatures):
    class ZeroLossWin:
        def __getitem__(_, i): 
            return fst_star(creatures, i)[1]

    min_attack = bisect(ZeroLossWin(), True, 4, 200)
    return fst_star(creatures, min_attack)[0]

TEST1 = '''#######
#.G...#
#...EG#
#.#.#G#
#..G#E#
#.....#
#######'''.split()

TEST2 = '''#######
#E..EG#
#.#G.E#
#E.##E#
#G..#.#
#..E#.#
#######'''.split()

if __name__ == '__main__':
    assert fst_star(parse(TEST1))[0] == 27730
    assert fst_star(parse(TEST2))[0] == 39514
    assert snd_star(parse(TEST1)) == 4988
    assert snd_star(parse(TEST2)) == 31284

    creatures = parse(open('data/day15.in'))
    print(fst_star(creatures)[0])
    print(snd_star(creatures))
