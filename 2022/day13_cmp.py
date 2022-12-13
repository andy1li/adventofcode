# https://adventofcode.com/2022/day/13

from itertools import chain
from functools import cmp_to_key

def parse_pairs(raw):
    def parse_pair(raw):
        return tuple(map(eval, raw.splitlines()))
    return list(map(parse_pair, raw.split('\n\n')))

def cmp(a, b):
    if type(a) == type(b) == list:
        n, m = len(a), len(b)
        for i in range(max(n, m)):
            if i >= n: return -1
            if i >= m: return 1
            if res := cmp(a[i], b[i]): 
                return res
        return 0
            
    elif type(a) == type(b) == int:
        return (a > b) - (a < b) 

    elif type(a) == int: return cmp([a], b)
    elif type(b) == int: return cmp(a, [b])
    

def fst_star(pairs): 
    results = (cmp(l, r) for l, r in pairs)
    return sum( i 
        for i, result in enumerate(results, 1) 
        if result == -1
    )

def snd_star(pairs):
    dividers = [[2], [6]]
    packets = list(chain.from_iterable(pairs)) + dividers
    packets = sorted(packets, key=cmp_to_key(cmp))
    return (
        (packets.index(dividers[0]) + 1)
      * (packets.index(dividers[1]) + 1)
    )

TEST = '''\
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]'''

if __name__ == '__main__':
    pairs = parse_pairs(TEST)
    assert fst_star(pairs) == 13
    assert snd_star(pairs) == 140

    pairs = parse_pairs(open('data/day13.in').read())
    print(fst_star(pairs))
    print(snd_star(pairs))