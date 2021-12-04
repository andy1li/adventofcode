# https://adventofcode.com/2021/day/3

from collections import Counter
from copy import deepcopy

def reduce(grid):
    gamma = epsilon = ''
    for row in zip(*grid):
        cnt = Counter(row)
        if cnt['1'] >= cnt['0']: gamma += '1'; epsilon += '0'
        else                   : gamma += '0'; epsilon += '1'
    return gamma, epsilon

def fst_star(grid):
    gamma, epsilon = reduce(grid)
    return int(gamma, 2) * int(epsilon, 2)

def snd_star(grid):
    airs = [deepcopy(grid), deepcopy(grid)]
    modes = ['most', 'least']
    for i, mode in enumerate(modes):
        for j in range(len(airs[i][0])):
            reduced = reduce(airs[i])
            airs[i] = list(filter(
                lambda x: x[j] == reduced[i][j],
                airs[i]
            ))
            if len(airs[i]) == 1: break
    return int(airs[0][0], 2) * int(airs[1][0], 2)

TEST = '''\
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010'''.splitlines()

if __name__ == '__main__':
    assert fst_star(TEST) == 198
    assert snd_star(TEST) == 230

    grid = open('data/day03.in').readlines()
    print(fst_star(grid))
    print(snd_star(grid))