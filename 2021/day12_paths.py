# https://adventofcode.com/2021/day/12

from collections import defaultdict, Counter
from copy import deepcopy

def parse(raw):
    G = defaultdict(set)
    for line in raw:
        a, b = line.strip().split('-')
        G[a].add(b); G[b].add(a)
    return G

def fst_star(visited, node):
    return node not in visited

def snd_star(visited, node):
    cnt = Counter(c for v, c in visited.items() if v.islower())
    return (
        node != 'start' and (
        (visited[node]==0 and cnt[2] <= 1)
     or (visited[node]==1 and cnt[2] == 0)
    ))

def count(G, check=fst_star): 
    def recurse(visited, node):
        if node == 'end': return 1
        cnt = 0
        for nbr in G[node]:
            if nbr.isupper() or check(visited, nbr):
                new_visited = deepcopy(visited)
                new_visited[nbr] += 1
                cnt += recurse(new_visited, nbr)
        return cnt

    return recurse(Counter(['start']), 'start')

TEST0 = '''\
start-A
start-b
A-c
A-b
b-d
A-end
b-end'''.splitlines()

TEST1 = '''\
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc'''.splitlines()

TEST2 = '''\
fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW'''.splitlines()

if __name__ == '__main__':
    assert count(parse(TEST0)) == 10
    assert count(parse(TEST1)) == 19
    assert count(parse(TEST2)) == 226
    assert count(parse(TEST0), snd_star) == 36
    assert count(parse(TEST1), snd_star) == 103
    assert count(parse(TEST2), snd_star) == 3509

    G = parse(open('data/day12.in'))
    print(count(G))
    print(count(G, snd_star))