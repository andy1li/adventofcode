# https://adventofcode.com/2022/day/11

from copy import deepcopy
from math import prod

MOD = 0

class Monkey:
    def __init__(self, items, op, mod, divisible, not_divisible):
        self.items = items
        self.op = op
        self.mod = mod
        self.divisible = divisible
        self.not_divisible = not_divisible
        self.count = 0

    def step(self, relief):
        self.count += len(self.items)
        for old in self.items:
            item = eval(self.op) 
            if relief: item //= 3
            if MOD: item %= MOD
            dst = self.not_divisible if item % self.mod else self.divisible
            yield dst, item
        self.items = []

    def __repr__(self):
        return str(self.items)

def parse_monkeys(raw):
    def parse_monkey(raw):
        _, items, op, mod, divisible, not_divisible = raw.splitlines()
        return Monkey(
            list(map(int, items.strip('Starting items: ').split(', '))), 
            op[19:], 
            int(mod[21:]), 
            int(divisible[29:]), 
            int(not_divisible[30:])
        )
    return list(map(parse_monkey, raw.split('\n\n')))

def round(monkeys, relief=True):
    for m in monkeys:
        for dst, item in m.step(relief):
            monkeys[dst].items += item,

def monkey_business(monkeys):
    counts = (m.count for m in monkeys)
    top_two = sorted(counts)[-2:]
    return top_two[0] * top_two[1]

def fst_star(monkeys):
    global MOD; MOD = 0
    monkeys = deepcopy(monkeys)
    for _ in range(20): round(monkeys)
    return monkey_business(monkeys)
    
def snd_star(monkeys):
    global MOD; MOD = prod(m.mod for m in monkeys)
    for _ in range(10000): round(monkeys, False)
    return monkey_business(monkeys)

if __name__ == '__main__':
    monkeys = parse_monkeys(open('data/day11_test.in').read())
    assert fst_star(monkeys) == 10605
    # assert snd_star(monkeys) == 2713310158

    monkeys = parse_monkeys(open('data/day11.in').read())
    print(fst_star(monkeys))
    print(snd_star(monkeys))