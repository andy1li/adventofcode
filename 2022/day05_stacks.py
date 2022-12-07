# https://adventofcode.com/2022/day/5

import re
from collections import namedtuple
from copy import deepcopy

Move = namedtuple('Move', 'n src dst')

def parse_stacks(stacks):
    reverse = reversed(stacks.splitlines())
    n = max(map(int, next(reverse).split()))
    stacks = [None] + [[] for _ in range(n)]
    for line in reverse:
        for i in range(n):
            x = line[1 + i*4]
            if x != ' ': stacks[i+1].append(x)
    return stacks

def parse_moves(moves):
    def parse_move(move):
        PATTERN = r'move (\d+) from (\d+) to (\d+)'
        return Move(*map(int, re.match(PATTERN, move).groups()))
    return [*map(parse_move, moves.splitlines())]

def parse(raw):
    stacks, moves = raw.split('\n\n')
    return parse_stacks(stacks), parse_moves(moves)

def fst_star(stacks, moves): 
    stacks = deepcopy(stacks)
    for move in moves:
        block = [stacks[move.src].pop() for _ in range(move.n)]
        stacks[move.dst] += block
    return ''.join(s.pop() for s in stacks[1:])

def snd_star(stacks, moves):
    stacks = deepcopy(stacks)
    for move in moves:
        block = [stacks[move.src].pop() for _ in range(move.n)]
        stacks[move.dst] += list(reversed(block))
    return ''.join(s.pop() for s in stacks[1:])

TEST = '''\
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''

if __name__ == '__main__':
    stacks, moves = parse(TEST)
    assert fst_star(stacks, moves) == 'CMZ'
    assert snd_star(stacks, moves) == 'MCD'

    stacks, moves = parse(open('data/day05.in').read())
    print(fst_star(stacks, moves))
    print(snd_star(stacks, moves))
