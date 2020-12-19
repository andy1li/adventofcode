# https://adventofcode.com/2020/day/18
# Originally from @heptaflex https://www.reddit.com/r/adventofcode/comments/kfh5gn/

import ast

class Xformer(ast.NodeTransformer): 
    def visit_Sub(_, __): return ast.Mult() 
    def visit_Mult(_, __): return ast.Add()

def evaluate(expr, add_first=False):
    expr = expr.replace("*", "-")
    if add_first: expr = expr.replace("+", "*")

    root = ast.parse(expr, mode='eval')
    root = Xformer().visit(root)
    return eval(compile(root, '', mode='eval'))

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
