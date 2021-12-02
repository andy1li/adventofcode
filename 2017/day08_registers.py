# https://adventofcode.com/2017/day/8

from collections import defaultdict
import re

def run(code):
    reg = defaultdict(int)
    highest = -float('inf')
    for line in code:
        action, condition = line.split(' if ')
        action = action.replace('inc', '+=')
        action = action.replace('dec', '-=')
        action = re.sub(r'([A-Za-z]+)', r'reg["\1"]', action)
        condition = re.sub(r'([A-Za-z]+)', r'reg["\1"]', condition)
        if eval(condition): exec(action)
        highest = max(highest, max(reg.values()))

    return max(reg.values()), highest

TEST = '''b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10'''.splitlines()

if __name__ == '__main__':
    assert run(TEST) == (1, 10)

    print(run(open('data/day08.in')))