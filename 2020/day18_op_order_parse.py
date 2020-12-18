# https://adventofcode.com/2020/day/18

from math import prod
from operator import add, mul

def parse(raw):
    def parse(raw, i=0):
        tree = []
        while i < len(raw):
            x = raw[i]
            if x == '(': 
                sub_tree, i = parse(raw, i+1)
                tree.append(['expr', sub_tree])
            elif x.isdigit():
                tree.append(['int', int(x)])
            elif x in '+*': 
                op = {'+': add, '*': mul}[x]
                tree.append(['op', op])
            elif x == ')': return tree, i
            i += 1
        return tree

    return [*map(parse, raw)]

def same_precedence(tree):
    acc, op = 0, add
    for label, node in tree:
        if label == 'int' : acc = op(acc, node)
        if label == 'expr': acc = op(acc, same_precedence(node))
        if label == 'op'  : op = node
    return acc

def add_first(tree):
    multiplicands = []
    iterator = iter(tree)
    for label, node in iterator:
        if label == 'int': multiplicands.append(node)
        if label == 'expr': multiplicands.append(add_first(node))
        if label == 'op' and node == add:
            nxt_lbl, nxt_nd = next(iterator)
            nxt_val = nxt_nd if nxt_lbl == 'int' else add_first(nxt_nd)
            multiplicands.append(multiplicands.pop() + nxt_val)
    return prod(multiplicands)

TEST = '''\
1 + 2 * 3 + 4 * 5 + 6
1 + (2 * 3) + (4 * (5 + 6))
2 * 3 + (4 * 5)
5 + (8 * 3 + 9 + 3 * 4 * 3)
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'''.splitlines()

if __name__ == '__main__':
    assert [*map(same_precedence, parse(TEST))] == [71, 51, 26, 437, 12240, 13632]
    assert [*map(add_first, parse(TEST))] == [231, 51, 46, 1445, 669060, 23340]
    trees = parse(open('data/day18.in'))
    print(sum(map(same_precedence, trees)))
    print(sum(map(add_first, trees)))