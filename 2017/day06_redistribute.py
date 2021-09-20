# https://adventofcode.com/2017/day/6

from itertools import count
import numpy as np

def parse(raw):
    return np.array(list(map(int, raw.split())))

def step(memory):
    mx, amx = memory.max(), memory.argmax()
    n, memory[amx] = len(memory), 0
    factor = mx // n
    memory += factor
    for i in range(amx+1, amx+1+(mx-factor*n)):
        memory[i % n] += 1
    return memory

def solve(memory):
    seen, memory = {}, memory.copy()
    for i in count():
        t_m = tuple(memory)
        if t_m in seen: return i, i-seen[t_m]
        seen[t_m] = i
        memory = step(memory)

if __name__ == '__main__':
    assert solve(parse('0 2 7 0')) == (5, 4)

    memory = parse(open('data/day06.in').read())
    print(solve(memory))