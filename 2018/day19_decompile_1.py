# https://adventofcode.com/2018/day/19

from day16_opcodes import Operation, op

OPCODES = {
    'addr': 'addrr', 'banr': 'and_rr', 'setr': 'setr_', 
    'addi': 'addri', 'bani': 'and_ri', 'seti': 'seti_',
    'mulr': 'mulrr', 'borr': 'or_rr',  # gt/eq * 6
    'muli': 'mulri', 'bori': 'or_ri',
}

def parse_op(line):
    code, A, B, C = line.split()
    code = OPCODES.get(code, code)
    return Operation(op(code), *map(int, [A, B, C]))

def parse(input):
    # input = input.split('\n')
    ip = int(next(input).split()[1])
    ops = [*map(parse_op, input)]
    return ip, ops

def simulate(ip, ops, regs=[0]*6):
    while 0 <= regs[ip] < len(ops):
        i = regs[ip]; op = ops[i]
        regs = op.code(regs, op)
        regs[ip] += 1
    return regs[0]

def sum_divisor(n): 
    return sum( i
        for i in range(1, n+1)
        if not n % i
    )

TEST = '''#ip 0
seti 5 0 1
seti 6 0 2
addi 0 1 0
addr 1 2 3
setr 1 0 0
seti 8 0 4
seti 9 0 5'''.split('\n')

if __name__ == '__main__':
    assert simulate(*parse(iter(TEST))) == 7
    assert sum_divisor(1010) == 1836

    # [0, 1010, 1, 1, 174, 3] -> [1836, 1010, 1011, 1011, True, 257]
    # print(simulate(*parse(open('data/day19.in'))))
    print(sum_divisor(1010))

    # [0, 10551410, 1, 1, 10550400, 3] -> ?
    # print(simulate(*parse(open('data/day19.in')), [1]+[0]*5))
    print(sum_divisor(10551410))
 