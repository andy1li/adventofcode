# https://adventofcode.com/2017/day/7

from collections import defaultdict
import re

def parse(raw):
    W, P, T = {}, {}, defaultdict(list)
    for line in raw:
        disc, *children = re.findall(r'[A-Za-z]+', line)
        weight = re.findall(r'\d+', line)[0]
        W[disc] = int(weight)
        for child in children: 
            P[child] = disc
            T[disc].append( child )
    return W, P, T

def find_head(P, W):
    return next(disc for disc in W if disc not in P)

def find_wrong(T, W, head):

    def recurse(disc):
        if not T[disc]: return W[disc]

        children_weights = {
            child: recurse(child)
            for child in T[disc]
        }

        weights = children_weights.values()
        if len(set(weights)) > 1: 
            for disc, weight in children_weights.items():
                copied = children_weights.copy()
                del copied[disc]
                set_weights = set(copied.values())
                if len(set_weights) == 1:
                    raise ValueError(
                        W[disc] 
                    - (children_weights[disc] - set_weights.pop())
                    )

        return sum(weights) + W[disc]

    try: recurse(head)
    except ValueError as e:
        return int(str(e))

TEST = '''pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)'''.splitlines()

if __name__ == '__main__':
    W, P, T = parse(TEST)
    head = find_head(P, W); assert head == 'tknk'
    assert find_wrong(T, W, head) == 60

    W, P, T = parse(open('data/day07.in'))
    head = find_head(P, W); print(head)
    print(find_wrong(T, W, head))