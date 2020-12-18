# https://adventofcode.com/2020/day/18
# originally from @ sciyoshi https://www.reddit.com/r/adventofcode/comments/kfeldk/2020_day_18_solutions/gg81308

import re

class Int(int):
    def __sub__(self, other): return Int(int(self) * other)
    def __mul__(self, other): return Int(int(self) + other)
    def __add__(self, other): return Int(int(self) + other)

def evaluate(expr, add_first=False):
    expr = re.sub(r"(\d+)", r"Int(\1)", expr)
    expr = expr.replace("*", "-")
    if add_first: expr = expr.replace("+", "*")
    return eval(expr, {"Int": Int})

TEST = '''\
1 + 2 * 3 + 4 * 5 + 6
1 + (2 * 3) + (4 * (5 + 6))
2 * 3 + (4 * 5)
5 + (8 * 3 + 9 + 3 * 4 * 3)
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'''.splitlines()

if __name__ == '__main__':
    assert [*map(evaluate, TEST)] == [71, 51, 26, 437, 12240, 13632]
    assert [evaluate(e, add_first=True) for e in TEST] == [231, 51, 46, 1445, 669060, 23340]
    expressions = open('data/day18.in').readlines()
    print(sum(map(evaluate, expressions)))
    print(sum(evaluate(e, add_first=True) for e in expressions))