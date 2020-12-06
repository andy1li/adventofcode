# https://adventofcode.com/2020/day/6

from functools import reduce

def parse(groups):
    return [*map(str.split, groups.split('\n\n'))]

def count(groups, fn):
    reducer = lambda g: reduce(fn, map(set, g))
    sets = map(reducer, groups)
    return sum(map(len, sets))

TEST = '''\
abc

a
b
c

ab
ac

a
a
a
a

b'''

if __name__ == '__main__':
    assert count(parse(TEST), set.union) == 11
    assert count(parse(TEST), set.intersection) == 6
    groups = parse(open('data/day06.in').read())
    print(count(groups, set.union))
    print(count(groups, set.intersection))