# https://adventofcode.com/2020/day/8

def parse(raw):
    def parse_line(line):
        op, arg = line.split(' ')
        return [op, int(arg)]
    return [*map(parse_line, raw)]

def run(code): 
    ip = acc = 0
    while ip < len(code):
        op, arg = code[ip]
        yield ip, acc
        if op == 'acc': acc += arg
        if op == 'jmp': ip += (arg-1)
        ip += 1
    yield -1, acc

def is_loop(code):
    seen = [0] * len(code)
    for ip, acc in run(code):
        if ip == -1: return False, acc
        if seen[ip]: return True, acc
        seen[ip] = 1

def fix(code):
    def toggle(i):
        op = code[i][0]
        if op == 'nop': code[i][0] = 'jmp'
        if op == 'jmp': code[i][0] = 'nop'

    def attempt(i): 
        toggle(i); loop, acc = is_loop(code)
        toggle(i); return loop, acc

    attempts = map(attempt, range(len(code)))
    return next( acc for loop, acc in attempts if not loop )

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