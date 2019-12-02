# https://adventofcode.com/2018/day/19

from day16_opcodes import Operation, op

CODES = {
    'addr': 'addrr', 'mulr': 'mulrr', 'setr': 'setr_', 
    'addi': 'addri', 'muli': 'mulri', 'seti': 'seti_',
    'banr': 'and_rr', 'borr': 'or_rr',
    'bani': 'and_ri', 'bori': 'or_ri',
}

def parse_op(line):
    code, A, B, C = line.split()
    code = CODES.get(code, code)
    return Operation(op(code), *map(int, [A, B, C]))

def parse(input):
    input = input.split('\n')
    ip = int(input[0].split()[1])
    ops = [*map(parse_op, input[1:])]
    return ip, ops

def fst_star(ip, ops, regs=[0]*6):
    while 0 <= regs[ip] < len(ops):
        i = regs[ip]; op = ops[i]
        regs = op.code(regs, op)
        regs[ip] += 1
    return regs[0]

def snd_star(n): 
    'Sum of divisors'
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
seti 9 0 5'''

if __name__ == '__main__':
    assert fst_star(*parse(TEST)) == 7
    assert snd_star(1010) == 1836

    # [0, 1010, 1, 1, 174, 3] -> [1836, 1010, 1011, 1011, True, 257]
    print(fst_star(*parse(open('data/day19.in').read())))

    # [0, 10551410, 1, 1, 10550400, 3] -> ?
    # print(fst_star(*parse(open('data/day19.in').read()), [1]+[0]*5))
    print(snd_star(10551410))
 