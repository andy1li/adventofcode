# https://adventofcode.com/2018/day/21

from bitarray import bitarray
from day19_decompile_1 import parse

def crack(ip, ops):
    regs = [0] * 6
    while 0 <= regs[ip] < len(ops):
        if regs[5] == 28: return regs[4]
        i = regs[ip]; op = ops[i]
        regs = op.code(regs, op)
        regs[ip] += 1

def repeat_hash():
    seen = bitarray(int(2**24))
    hash = last_hash = 0

    while True: # r0 != hash
        sword  = hash | 65536 # set bit 17
        hash = 2024736

        while sword:
            sword, byte = divmod(sword, 256) # pop byte
            hash = ((hash + byte) * 65899) % 16777216 # 24-bit (3 bytes)
            
        # print('hash:', hash)
        if seen[hash]: return last_hash
        seen[hash] = 1; last_hash = hash

if __name__ == '__main__':
    print(crack(*parse(open('data/day21.in'))))
    print(repeat_hash())
