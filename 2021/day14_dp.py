# https://adventofcode.com/2021/day/14

from collections import Counter
from functools import cache

def parse(raw):
    return dict(line.split(' -> ') for line in raw)

@cache
def recurse(a, b, n):
    if n == 0 or (a+b not in rules): 
        return Counter(b)
    c = rules[a+b]
    return recurse(a, c, n-1) + recurse(c, b, n-1)

def build(rules, polymer, n=10): 
    cnt = Counter(polymer[0])
    for a, b in zip(polymer, polymer[1:]):
        cnt += recurse(a, b, n)
        
    freq = sorted(cnt.values())
    return freq[-1] - freq[0]

TEST = '''\
CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C'''.splitlines()

if __name__ == '__main__':
    rules = parse(TEST)
    assert build(rules, 'NNCB') == 1588
    assert build(rules, 'NNCB', 40) == 2188189693529
    recurse.cache_clear()

    start = 'KBKPHKHHNBCVCHPSPNHF'
    rules = parse(open('data/day14.in').read().splitlines())
    print(build(rules, start))
    print(build(rules, start, 40))