# https://adventofcode.com/2020/day/6

def parse(raw):
    parse_group = lambda g: [*map(set, g.split())]
    return [*map(parse_group, raw.split('\n\n'))]

def count(groups, fn):
    return sum( len(fn(*g)) for g in groups )

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