# https://adventofcode.com/2019/day/5

from functools import partial
from operator  import add, mul, truth, not_, lt, eq

INSTRUCTION = {
    1: (add,   4), 
    2: (mul,   4), 
    3: (None,  2), # save input
    4: (None,  2), # push output
    5: (truth, 0), # jump-if-true
    6: (not_,  0), # jump-if-false
    7: (lt,    4),
    8: (eq,    4), 
    9: (None,  2)  # adjust the relative base
}

def parse_modes(op):
    op = str(op).zfill(5)
    return int(op[-2:]), [*map(int, reversed(op[:-2]))]

def run(code, input, extra=1024*4): 
    mem = code.copy() + [0] * extra
    input = iter(input)
    
    ip = rb = 0
    while mem[ip] != 99:
        op, modes = parse_modes(mem[ip])
        func, length = INSTRUCTION[op]
        p = mem[ip+1:ip+4]

        def v(i):
            if modes[i] == 0: return mem[p[i]]
            if modes[i] == 1: return p[i]
            if modes[i] == 2: return mem[rb+p[i]]
        def a(i):
            return p[i] if modes[i] < 2 else rb+p[i]

        if op in [1, 2, 7, 8]: mem[a(2)] = int(func(v(0), v(1)))
        elif op == 3         : mem[a(0)] = next(input)
        elif op == 4         : yield v(0)
        elif op in [5, 6]    : ip = v(1) if func(v(0)) else ip+3
        elif op == 9         : rb += v(0)
  
        ip += length