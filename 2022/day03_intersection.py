# https://adventofcode.com/2022/day/3

from string import ascii_lowercase, ascii_uppercase
from typing import Set, Tuple 

Rucksack = Tuple[Set[str], Set[str]]

def compartments(line) -> Rucksack:
    length = len(line)
    return set(line[:length//2]), set(line[length//2:])
        
def priority(xs):
    item = set.intersection(*xs).pop()
    return f'_{ascii_lowercase}{ascii_uppercase}'.index(item)

def fst_star(raw): 
    return sum(map(priority, map(compartments, raw)))

def snd_star(raw):
    groups = (raw[i:i+3] for i in range(0, len(raw), 3))
    groups = ([*map(set, g)] for g in groups)
    return sum(map(priority, groups))

TEST = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''.splitlines()

if __name__ == '__main__':
    assert fst_star(TEST) == 157
    assert snd_star(TEST) == 70

    rucksacks = open('data/day03.in').read().splitlines()
    print(fst_star(rucksacks))
    print(snd_star(rucksacks))