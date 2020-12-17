# https://adventofcode.com/2020/day/14

from itertools import chain
import re

def to_bin(x): return list(bin(int(x))[2:].zfill(36))

def to_int(x): return int(''.join(x), 2)

def parse(line):
    if line.startswith('mask'): 
        return 'mask', line.split()[-1]
    if line.startswith('mem'): 
        addr, val = map(int, re.findall(r'\d+', line))
        return 'mem', (addr, val)

def masked_val(mask, val):
    return to_int(
        v if m == 'X' else m
        for i, (m, v) in enumerate(zip(mask, to_bin(val)))
    )

def masked_addrs(mask, addr):
    def extend(a):
        if bit == 'X': return [a+'0', a+'1']
        else: return [a + str(int(bit) or addr[i])]

    addr, addrs = to_bin(addr), ['']
    for i, bit in enumerate(mask):
        addrs = chain(*map(extend, addrs))
    yield from map(to_int, addrs)
    
def run(get_addrs, get_val, code): 
    mask, mem = '', {}
    for op, param in code:
        if op == 'mask': mask = param
        if op == 'mem': 
            addr, val = param
            for a in get_addrs(mask, addr):
                mem[a] = get_val(mask, val)
    return sum(mem.values())

def fst_star(code):
    id_addr = lambda _, x: [x]
    return run(id_addr, masked_val, code)

def snd_star(code):
    id_val = lambda _, x: x
    return run(masked_addrs, id_val, code)

TEST1 = '''\
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0'''.splitlines()

TEST2 = '''\
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1'''.splitlines()

if __name__ == '__main__':
    assert fst_star(map(parse, TEST1)) == 165
    assert snd_star(map(parse, TEST2)) == 208
    code = [*map(parse, open('data/day14.in'))]
    print(fst_star(code))
    print(snd_star(code))