# https://adventofcode.com/2019/day/6

from collections import defaultdict

def parse(input):
    start = end = None
    T, G = defaultdict(set), defaultdict(set)
    for line in input:
        a, b = line.strip().split(')')
        T[a].add(b)
        G[a].add(b); G[b].add(a)
        if b == 'YOU': start = a
        if b == 'SAN': end = a  

    return T, G, start, end

def fst_star(T, *_):
    def recurse(x, d=0):
        return len(T[x]) * (d+1) + sum(
           recurse(y, d+1) for y in T[x]
        )
    return recurse('COM')

def snd_star(_, G, start, end): 
    q, seen = [(0, start)], set([start])
    for d, x in q:
        if x == end: return d
        for y in G[x]:
            if y in seen: continue
            seen.add(y)
            q.append((d+1, y))

TEST1 = '''COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L'''.split('\n')
TEST2 = '''COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN'''.split('\n')

if __name__ == '__main__':
    assert fst_star(*parse(TEST1)) == 42
    assert snd_star(*parse(TEST2)) == 4

    data = parse(open('data/day06.in'))
    print(fst_star(*data))
    print(snd_star(*data))