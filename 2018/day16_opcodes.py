# https://adventofcode.com/2018/day/16

from typing import List, NamedTuple
import operator
import re

Registers = List[int]

class Operation(NamedTuple):
    code: int
    A: int; B: int; C: int

class Sample(NamedTuple):
    op: Operation
    before: Registers
    after: Registers

def parse_sample(input):
    before = re.match(r'Before: \[(\d), (\d), (\d), (\d)\]', input[0]).groups()
    after  = re.match(r'After:  \[(\d), (\d), (\d), (\d)\]', input[2]).groups()
    return Sample(
        Operation(*map(int, input[1].split())),
        [*map(int, before)], 
        [*map(int, after)],
    )

def parse(input):
    input = input.split('\n')
    samples = [
        parse_sample(input[i:i+4])
        for i in range(0, len(input), 4)
    ]
    return samples

def op(opcode):
    operator_name, a_type, b_type = opcode[:-2], opcode[-2], opcode[-1]
    try: func = getattr(operator, operator_name)
    except AttributeError: func = lambda A, _: A # 'set' not in operator
    
    def operate(regs, op):
        regs = regs[:]
        regs[op.C] = func(
            regs[op.A] if a_type == 'r' else op.A,
            regs[op.B] if b_type == 'r' else op.B
        )
        return regs
    return operate

ALL_OPS = [*map(op, [
    'addrr', 'and_rr', 'setr_', 'seti_',
    'addri', 'and_ri', 'gtir', 'eqir', 
    'mulrr', 'or_rr',  'gtri', 'eqri',
    'mulri', 'or_ri',  'gtrr', 'eqrr'         
])]

def possible_ops(sample):
    return set( op
        for op in ALL_OPS
        if op(sample.before, sample.op) == sample.after
    )

def fst_star(samples):
    return sum(len(possible_ops(s))>=3 for s in samples)

def snd_star(samples):
    ops = {
        opcode: set(ALL_OPS)
        for opcode in range(16)
    }
    # Eliminate
    for sample in samples:
        ops[sample.op.code] &= possible_ops(sample)

        if len(ops[sample.op.code]) == 1:
            for i in range(16):
                if i == sample.op.code: continue
                ops[i] -= ops[sample.op.code]
    # Finalize
    for opcode in ops: 
        ops[opcode] = ops[opcode].pop()

    # Run the test program
    regs = [0, 0, 0, 0]
    for line in open('data/day16b.in'):
        op = Operation(*map(int, line.split()))
        regs = ops[op.code](regs, op)
    return regs

TEST = '''Before: [3, 2, 1, 1]
9 2 1 2
After:  [3, 2, 2, 1]
'''

if __name__ == '__main__':
    assert fst_star(parse(TEST)) == 1

    samples = parse(open('data/day16a.in').read())
    print(fst_star(samples))
    print(snd_star(samples))