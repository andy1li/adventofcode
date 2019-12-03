# https://adventofcode.com/2019/day/2

from itertools import product
from operator  import add, mul

OPERATION = {1: add, 2: mul}

def fst_star(original, noun=12, verb=2): 
    code = original.copy()
    i, code[1], code[2] = 0, noun, verb
    while code[i] != 99:
        op, a, b, d = code[i:i+4]
        code[d] = OPERATION[op](code[a], code[b])
        i += 4
    return code[0]

def snd_star(code):
    for noun, verb in product(range(100), repeat=2):
        if fst_star(code, noun, verb) == 19690720:
            return 100*noun + verb

if __name__ == '__main__':
    code = [*map(int, open('data/day02.in').read().split(','))]
    print(fst_star(code))
    print(snd_star(code))
