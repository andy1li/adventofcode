# https://adventofcode.com/2020/day/12

import numpy as np

DIR = 'ESWN'
DELTA = {
    'E':  np.array([1, 0]), 'W':  np.array([-1, 0]),
    'N':  np.array([0, 1]), 'S':  np.array([0, -1])
}

def parse(line): return line[0], int(line[1:])

def fst_star(instructions): 
    pos, d = np.zeros(2, int), 0
    for action, value in instructions:
        if action in 'LR': 
            cw = [-1, 1][action == 'R']
            d = (d + value//90 * cw) % 4
        if action == 'F': pos += DELTA[DIR[d]] * value
        if action in DIR: pos += DELTA[action] * value
    return sum(map(abs, pos))

def snd_star(instructions):
    def rotate(v, action, value):
        cw = [-1, 1][action == 'R']
        n = (value//90 * cw) % 4
        for _ in range(n): v = v[1], -v[0]
        return np.array(v)

    ship, v = np.zeros(2, int), np.array([10, 1])
    for action, value in instructions:
        if action in 'LR': v = rotate(v, action, value)
        if action == 'F': ship += v * value
        if action in DIR: v += DELTA[action] * value
    return sum(map(abs, ship))

TEST = '''\
F10
N3
F7
R90
F11'''.splitlines()

if __name__ == '__main__':
    assert fst_star(map(parse, TEST)) == 25
    assert snd_star(map(parse, TEST)) == 286
    instructions = [*map(parse, open('data/day12.in'))]
    print(fst_star(instructions))
    print(snd_star(instructions))