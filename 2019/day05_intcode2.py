# https://adventofcode.com/2019/day/5

from functools import partial
from operator  import add, mul, truth, not_, lt, eq

INSTRUCTION = {
    1: (add,   4), 
    2: (mul,   4), 
    3: (None,  2), # save input
    4: (None,  2), # ouput
    5: (truth, 0), # jump-if-true
    6: (not_,  0), # jump-if-false
    7: (lt,    4),
    8: (eq,    4)
}

def handle_modes(op):
    op = str(op).zfill(4)
    return int(op[-2:]), [*map(int, reversed(op[:-2]))]

def read(code, params, modes, idx):
    return params[idx] if modes[idx] else code[params[idx]]

def run(code, input): 
    code = code.copy()
    ip, output = 0, []
    while code[ip] != 99:
        op, modes = handle_modes(code[ip])
        func, length = INSTRUCTION[op]
        p = code[ip+1:ip+4]
        r = partial(read, code, p, modes)

        if op in [1, 2, 7, 8]: code[p[2]] = func(r(0), r(1))
        elif op == 3         : code[p[0]] = input
        elif op == 4         : output.append( code[p[0]] )
        elif op in [5, 6]    : ip = r(1) if func(r(0)) else ip+3

        ip += length

    return output

TEST = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]

if __name__ == '__main__':
    code = [*map(int, open('data/day05.in').read().split(','))]
    
    assert run([3,0,4,0,99], 1) == [1]

    # assert run(TEST, 1) == [999]
    assert run(TEST, 8) == [1000]
    assert run(TEST, 9) == [1001]

    print(run(code, 1))
    print(run(code, 5))