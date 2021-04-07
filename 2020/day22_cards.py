# https://adventofcode.com/2020/day/22

from copy import deepcopy
from collections import deque
from itertools import count

def parse(raw):
    def parse_deck(raw):
        deck = raw.splitlines()[1:]
        return deque(map(int, deck))
    return [*map(parse_deck, raw.split('\n\n'))]

def draw(decks):
    return [decks[i].popleft() for i in [0, 1]]

def can_recurse(decks, drawn):
    return all(drawn[i] <= len(decks[i]) for i in [0, 1])

def truncated(decks, drawn):
    return [deque(list(decks[i])[:drawn[i]]) for i in [0, 1]]

def step(decks, recusive):
    drawn = draw(decks)
    winner = (
        play(truncated(decks, drawn), recusive)
        if recusive and can_recurse(decks, drawn) else
        drawn[1] > drawn[0]
    )
    decks[winner] += [drawn[winner], drawn[1-winner]]
    return decks
    
def to_tuple(decks): 
    return tuple(map(tuple, decks))

def play(decks, recusive): 
    seen = set()
    while all(decks): 
        if to_tuple(decks) in seen: return 0
        seen.add(to_tuple(decks))
        decks = step(decks, recusive)
    return int(bool(decks[1]))

def score(decks, recusive=False):
    decks = deepcopy(decks)
    winner = decks[play(decks, recusive=recusive)]
    return sum(x * i for x, i in zip(reversed(winner), count(1)))

TEST = '''\
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10'''

TEST2 = '''\
Player 1:
43
19

Player 2:
2
29
14'''

if __name__ == '__main__':
    assert score(parse(TEST)) == 306
    assert score(parse(TEST), recusive=True) == 291
    decks = parse((open('data/day22.in').read()))
    print(score(decks))
    print(score(decks, recusive=True))

