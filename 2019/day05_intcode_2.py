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
    8: (eq,    4)
}

def parse_modes(op):
    op = str(op).zfill(4)
    return int(op[-2:]), [*map(int, reversed(op[:-2]))]

def run(code, input): 
    code, ip = code.copy(), 0
    while code[ip] != 99:
        op, modes = parse_modes(code[ip])
        func, length = INSTRUCTION[op]
        p = code[ip+1:ip+4]
        v = lambda i: p[i] if modes[i] else code[p[i]]

        if op in [1, 2, 7, 8]: code[p[2]] = func(v(0), v(1))
        elif op == 3         : code[p[0]] = next(input)
        elif op == 4         : yield v(0)
        elif op in [5, 6]    : ip = v(1) if func(v(0)) else ip+3

        ip += length

TEST = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]

if __name__ == '__main__':
    code = [*map(int, open('data/day05.in').read().split(','))]
    
    assert next(run([3,0,4,0,99], iter([1]))) == 1

    assert next(run(TEST, iter([1]))) == 999
    assert next(run(TEST, iter([8]))) == 1000
    assert next(run(TEST, iter([88]))) == 1001

    print(*run(code, iter([1])))
    print(*run(code, iter([5])))