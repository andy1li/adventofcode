# https://adventofcode.com/2017/day/6

from itertools import count
import numpy as np

def parse(raw):
    return np.array(list(map(int, raw.split())))

def step(memory):
    n, argmax_ = len(memory), np.argmax(memory)
    max_, memory[argmax_] = memory[argmax_], 0
    factor = max_ // n
    memory += factor
    for i in range(argmax_+1, argmax_+1+(max_-factor*n)):
        memory[i % n] += 1
    return memory

def solve(memory):
    seen, memory = {}, memory.copy()
    for i in count():
        if tuple(memory) in seen: 
            return i, i-seen[ tuple(memory) ]
        seen[ tuple(memory) ] = i
        memory = step(memory)

if __name__ == '__main__':
    assert solve(parse('0 2 7 0')) == (5, 4)

    memory = parse(open('data/day06.in').read())
    print(solve(memory))