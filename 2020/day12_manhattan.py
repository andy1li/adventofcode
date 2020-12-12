# https://adventofcode.com/2020/day/12

import numpy as np
import re

DIR = 'ESWN'
DELTA = {
    'E':  np.array([ 1, 0]), 'W':  np.array([-1, 0]),
    'N':  np.array([0,  1]), 'S':  np.array([0, -1])
}

def parse(line):
    action, value = re.match(r'([A-Z])(\d+)', line).groups()
    return action, int(value)

def fst_star(instructions): 
    pos, direction = np.array([0, 0]), 0
    for action, value in instructions:
        if action == 'L': direction = (direction - value//90) % 4
        if action == 'R': direction = (direction + value//90) % 4
        if action == 'F': pos += DELTA[DIR[direction]] * value
        if action in DIR: pos += DELTA[action] * value
    return sum(map(abs, pos))

def snd_star(instructions):
    def rotate(wp, action, value):
        n = (value//90 * [-1, 1][action == 'L'] + 4) % 4
        for _ in range(n):
            wp = np.array([-wp[1], wp[0]])
        return wp

    ship, wp = np.array([0, 0]), np.array([10, 1])
    for action, value in instructions:
        if action in 'LR': wp = rotate(wp, action, value)
        if action == 'F': ship += wp * value
        if action in DIR: wp += DELTA[action] * value    
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