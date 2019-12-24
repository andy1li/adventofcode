# https://adventofcode.com/2019/day/5

from collections import deque
from operator  import add, mul, truth, not_, lt, eq

INSTRUCTION = {
 # opcode: (func,  length)
        1: (add,   4), 
        2: (mul,   4), 
        3: (None,  2), # save input
        4: (None,  2), # send output
        5: (truth, 0), # jump-if-true
        6: (not_,  0), # jump-if-false
        7: (lt,    4),
        8: (eq,    4), 
        9: (None,  2)  # adjust the relative base
}

def parse_modes(op):
    op = str(op).zfill(5)
    return int(op[-2:]), [*map(int, reversed(op[:-2]))]

def run(code, input, callback=None, extra=1024*4): 
    memory = code.copy() + [0] * extra
    input = iter(input)
    if callback: out_queue = deque()

    def val(i):
        if modes[i] == 0: return memory[params[i]]
        if modes[i] == 1: return params[i]
        if modes[i] == 2: return memory[rb+params[i]]
    def addr(i):
        return params[i] if modes[i] < 2 else rb+params[i]
    
    ip = rb = 0
    while memory[ip] != 99:
        op, modes = parse_modes(memory[ip])
        func, length = INSTRUCTION[op]
        params = memory[ip+1:ip+4]

        if op in [1, 2, 7, 8]: 
            memory[addr(2)] = int(func(val(0), val(1)))

        elif op == 3: 
            memory[addr(0)] = next(input)
            if callback: yield

        elif op == 4 and callback:
            out_queue.append(val(0))
            if len(out_queue) >= 3: 
                callback(out_queue.popleft() for _ in range(3))
            yield

        elif op == 4      : yield val(0)
        elif op in [5, 6] : ip = val(1) if func(val(0)) else ip+3
        elif op == 9      : rb += val(0)
  
        ip += length