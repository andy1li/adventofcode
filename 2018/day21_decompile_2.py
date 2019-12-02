# https://adventofcode.com/2018/day/21

from bitarray import bitarray
from day19_decompile_1 import parse

def fst_star(ip, ops):
    regs = [0] * 6
    while 0 <= regs[ip] < len(ops):
        if regs[5] == 28: return regs[4]
        i = regs[ip]; op = ops[i]
        regs = op.code(regs, op)
        regs[ip] += 1

def snd_star():
    seen = bitarray(16774173+1)
    random = last_random = 0

    while 1: # r0 != random
        sword  = random | 65536
        random = 2024736

        while sword:
            sword, byte = divmod(sword, 256)
            random = ((random + byte) * 65899) % 16777216
             
        if seen[random]: return last_random
        seen[random] = 1; last_random = random

if __name__ == '__main__':
    print(fst_star(*parse(open('data/day21.in').read())))
    print(snd_star())
