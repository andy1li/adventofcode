# https://adventofcode.com/2022/day/9

import numpy as np
from itertools import chain
from copy import deepcopy

def parse_motions(raw):
    DELTAS = {        # x, y
        'L': np.array([-1, 0]),
        'R': np.array([ 1, 0]),
        'U': np.array([ 0,-1]),
        'D': np.array([ 0, 1]),
    }
    def parse_motion(line):
        d, x = line.split()
        return (DELTAS[d] for _ in range(int(x)))
    return list(chain.from_iterable(map(parse_motion, raw)))

def step(rope, motion):
    rope = deepcopy(rope)
    rope[0] += motion
    for i in range(len(rope)-1):
        pull = rope[i] - rope[i+1]
        if any(abs(x) > 1 for x in pull):
            rope[i+1] += pull // abs(pull)
    return rope

def solve(motions, n=10): 
    rope = [np.array([0, 0]) for _ in range(n)]
    history = set([(0, 0)])
    for m in motions:
        rope = step(rope, m) 
        history.add(tuple(rope[-1]))
    return len(history)

TEST0 = '''\
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2'''.splitlines()
TEST1 = '''\
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20'''.splitlines()

if __name__ == '__main__':
    assert solve(parse_motions(TEST0), n=2) == 13
    assert solve(parse_motions(TEST1)) == 36

    motions = parse_motions(open('data/day09.in'))
    print(solve(motions, n=2))
    print(solve(motions))