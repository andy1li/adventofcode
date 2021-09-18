# https://adventofcode.com/2017/day/5

from itertools import count

def parse(raw):
    return list(map(int, raw))

def increment(x): return x+1

def fluctuate(x): return x-1 if x>=3 else x+1

def count_steps(jumps, func=increment, ir=0):
    try:
        for i in count():
            jumps[ir], ir = func(jumps[ir]), jumps[ir]+ir
    except IndexError:
        return i

TEST = '0 3 0 1 -3'.split()

if __name__ == '__main__':
    assert count_steps(parse(TEST)) == 5
    assert count_steps(parse(TEST), fluctuate) == 10

    print(count_steps(parse(open('data/day05.in'))))
    print(count_steps(parse(open('data/day05.in')), fluctuate))