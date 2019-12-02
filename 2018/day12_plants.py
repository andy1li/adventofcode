# https://adventofcode.com/2018/day/12

from collections import defaultdict
from itertools import count

def parse(input):
    initial = next(input).strip().split(': ')[1]
    state = { i
        for i, pot in enumerate(initial)
        if pot == '#'
    }
    rules = set(); next(input)
    for line in input:
        pattern, result = line.strip().split(' => ')
        if result == '#': rules.add(pattern)
    return rules, state

def step(rules, state):
    start, end = min(state)-2, max(state)+3
    return { i
        for i in range(start, end)
        if ''.join(
            '#' if j in state else '.'
            for j in range(i-2, i+3)
        ) in rules        
    }

def to_string(state):
    start, end = min(state), max(state)+1
    return ''.join(
        '#' if i in state else '.'
        for i in range(start, end)
    ).strip('.')

def fst_star(rules, state):
    for _ in range(20): 
        state = step(rules, state)
    return sum(state)

def snd_star(rules, state, stop=158):
    for i in count(1): 
        state = step(rules, state)
        if to_string(state) == '##......##........##.......##....##.........##........##......##....##.............##....##........##.........##.............##........##...........##..........##.....##.....##.....##.....##':
            assert sum(step(rules, state)) - sum(state) == 42
            return 42*(50000000000-i) + sum(state)


TEST = '''initial state: #..#.#..##......###...###

...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #'''.split('\n')

if __name__ == '__main__':
    rules, state = parse(iter(TEST))
    assert fst_star(rules, state) == 325

    rules, state = parse(open('data/day12.in'))
    print(fst_star(rules, state))
    print(snd_star(rules, state))