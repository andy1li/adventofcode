# https://adventofcode.com/2020/day/22

from copy import deepcopy
from collections import deque
from itertools import islice

def parse(raw):
    parse_deck = lambda raw: deque(map(int, raw.splitlines()[1:]))
    return [*map(parse_deck, raw.split('\n\n'))]

def combat(drawn, decks, recusive):
    # optimization thanks to u/curious_sapi3n and u/Nomen_Heroum:
    # https://www.reddit.com/r/adventofcode/comments/khyjgv/2020_day_22_solutions/ggpcsnd/
    if recusive and all(drawn[i] <= len(decks[i]) for i in [0, 1]):
        subgame = [deque(islice(decks[i], drawn[i])) for i in [0, 1]] 
        if max(subgame[0]) > max(subgame[1]): return 0
        else: return play(subgame, recusive=True)
    else: 
        return drawn[1] > drawn[0]

to_tuple = lambda decks: tuple(map(tuple, decks))

def play(decks, recusive):
    seen = set()
    while all(decks):
        if to_tuple(decks) in seen: return 0
        seen.add(to_tuple(decks))

        drawn = [decks[i].popleft() for i in [0, 1]]    
        winner = combat(drawn, decks, recusive)
        decks[winner] += [drawn[winner], drawn[1-winner]]
    return bool(decks[1])

def score(decks, recusive=False):
    decks = deepcopy(decks)
    winner = decks[play(decks, recusive=recusive)]
    return sum(i * x for i, x in enumerate(reversed(winner), 1))

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