# https://adventofcode.com/2018/day/8

from itertools import islice

def parse_tree(input):
    n_children, n_meta = islice(input, 2)
    return {
        'children': [parse_tree(input) for _ in range(n_children)],
        'meta': [*islice(input, n_meta)]
    }

def fst_star(tree): 
    return sum(tree['meta']) + sum(
        fst_star(child)
        for child in tree['children']
    )

def snd_star(tree):
    if not tree['children']: return sum(tree['meta'])

    children_values = {
        i+1: snd_star(child)
        for i, child in enumerate(tree['children'])
    }
    return sum(
        children_values.get(m, 0)
        for m in tree['meta']
    )
    
if __name__ == '__main__':
    TEST = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'
    tree = parse_tree(map(int, TEST.split()))
    assert fst_star(tree) == 138
    assert snd_star(tree) == 66

    tree = parse_tree(map(int, open('data/day08.in').read().split()))
    print(fst_star(tree))
    print(snd_star(tree))