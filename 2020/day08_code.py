# https://adventofcode.com/2020/day/8

from copy import deepcopy

def parse(raw):
    def parse_line(line):
        op, arg = line.split(' ')
        return [op, int(arg)]
    return [*map(parse_line, raw)]

def run(code): 
    ip = acc = 0
    while True:
        op, arg = code[ip]
        yield ip, acc
        if op == 'acc': acc += arg
        if op == 'jmp': ip += (arg-1)
        ip += 1
        if ip >= len(code): 
            yield (-1, acc); return

def is_loop(code):
    seen = set()
    for ip, acc in run(code):
        if ip == -1: return False, acc
        if ip in seen: return True, acc
        seen.add(ip)

def fix(code):
    for i in range(len(code)):
        copy = deepcopy(code)
        op = copy[i][0]
        if   op == 'nop': copy[i][0] = 'jmp'
        elif op == 'jmp': copy[i][0] = 'nop'
        loop, acc = is_loop(copy)
        if not loop: return acc

TEST = '''\
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6'''.splitlines()

if __name__ == '__main__':
    assert is_loop(parse(TEST))[1] == 5
    assert fix(parse(TEST)) == 8
    code = parse(open('data/day08.in'))
    print(is_loop(code)[1])
    print(fix(code))