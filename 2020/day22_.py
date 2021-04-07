# https://adventofcode.com/2020/day/22

from collections import deque
from itertools import count

def parse(raw):
    def parse_deck(raw):
        deck = raw.splitlines()[1:]
        return deque(map(int, deck))
    return [*map(parse_deck, raw.split('\n\n'))]

def fst_star(decks): 
    while all(decks):
        round = decks[0].popleft(), decks[1].popleft()
        win = round[1] > round[0]
        decks[win].extend(sorted(round, reverse=True))
    winner = decks[0] or decks[1]
    return sum(x * i for x, i in zip(reversed(winner), count(1)))

def snd_star(decks):
    pass

TEST1 = '''\
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
    assert fst_star(parse(TEST1)) == 306
    snd_star(parse(TEST2))
    # print(fst_star(parse(open('data/day22.in').read())))
    # print(snd_star(data))

