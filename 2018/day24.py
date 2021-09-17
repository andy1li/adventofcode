# https://adventofcode.com/2018/day/24

import re
from bisect import bisect_left as bisect
from copy import deepcopy

class Group:
    def __init__(self, raw, army):
        PATTERN = r'(\d+) units each with (\d+) hit points (?:\(([\w,; ]+)\))?\s?with an attack that does (\d+) ([a-zA-Z]+) damage at initiative (\d+)'
        data = re.match(PATTERN, raw).groups()
        self.army = army
        self.units = int(data[0])
        self.hp = int(data[1])
        self.attack_damage = int(data[3])
        self.attack_type = data[4]
        self.initiative = int(data[5])
        self.target = None
        self.targeted_by = None
        self.immune = set()
        self.weak = set()
        if data[2]:
            for x in data[2].split('; '):
                special, types = x.split(' to ')
                setattr(self, special, set(types.split(', ')))

    def __repr__(self):
        return f'{self.units} {self.army} ✖ {{💪: {self.effective_power}, ⚡️: {self.initiative}, ❤️: {self.units}, {self.attack_type}: {self.attack_damage}, immune: {self.immune}, weak: {self.weak}}}'

    @property
    def effective_power(self): 
        return self.units * self.attack_damage

    @property
    def is_alive(self): 
        return self.units > 0

    def boost(self, value):
        self.attack_damage += value

    def effective_damage(self, other):
        if self.attack_type in other.immune: return 0
        ratio = 1 + int(self.attack_type in other.weak)
        return self.effective_power * ratio

    def select_target(self, groups):
        self.target = None
        enemies = (
            filter_army(groups, 'Immune') 
            if self.army == 'Infection' else 
            filter_army(groups, 'Infection')
        )
        select = lambda other: (
            self.effective_damage(other),
            other.effective_power,
            other.initiative
        )
        target = max(
            filter(lambda g: not g.targeted_by, enemies),
            key=select, default=None
        )
        if not target or self.effective_damage(target) == 0: return
        self.target = target
        target.targeted_by = self

    def attack(self):
        if self.is_alive and self.target:
            self.target.got_hit(
                self.effective_damage(self.target)
            )

    def got_hit(self, damage):
        killed = damage // self.hp
        self.units -= min(self.units, killed)

def parse_army(input, army):
    return [Group(line, army) for line in input]

def parse_groups(a, b):
    return parse_army(a, 'Immune') + parse_army(b, 'Infection')

def not_end(groups):
    return len(set(g.army 
        for g in groups
        if g.is_alive
    )) == 2

def filter_army(groups, army):
    return { g
        for g in groups
        if g.army == army
        and g.is_alive
    }

def combat_outcome(groups, boost=0):
    gs = deepcopy(groups)
    for g in gs: 
        if g.army == 'Immune': g.boost(boost)
    # print(*gs, sep='\n\n', end='\n\n\n')
    prev = [(g.army, g.units) for g in gs]
    while not_end(gs):
        for g in gs: 
            g.targeted_by = None
        for g in sorted(gs, key=lambda g: -g.effective_power): 
            g.select_target(gs)
        for g in sorted(gs, key=lambda g: -g.initiative):
            g.attack()

        gs = list(filter(lambda g: g.is_alive, gs))

        curr = [(g.army, g.units) for g in gs]
        if prev == curr: return -1, 'Draw'
        prev = curr
        
    return sum(g.units for g in gs), gs[0].army

def min_boost(groups):
    class ImmuneWin:
        def __getitem__(self, i): 
            return combat_outcome(groups, i)[1] == 'Immune'

    boost = bisect(ImmuneWin(), True, 1, 2000)
    return combat_outcome(groups, boost)[0]

TEST_A = '''17 units each with 5390 hit points (weak to radiation, bludgeoning) with an attack that does 4507 fire damage at initiative 2
989 units each with 1274 hit points (immune to fire; weak to bludgeoning, slashing) with an attack that does 25 slashing damage at initiative 3'''.splitlines()

TEST_B = '''801 units each with 4706 hit points (weak to radiation) with an attack that does 116 bludgeoning damage at initiative 1
4485 units each with 2961 hit points (immune to radiation; weak to fire, cold) with an attack that does 12 slashing damage at initiative 4'''.splitlines()

if __name__ == '__main__':
    groups = parse_groups(TEST_A, TEST_B)
    assert combat_outcome(groups)[0] == 5216    
    assert min_boost(groups) == 51

    groups = parse_groups(open('data/day24a.in'), open('data/day24b.in'))
    print(combat_outcome(groups)[0])
    print(min_boost(groups))

    

    