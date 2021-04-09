# https://adventofcode.com/2020/day/23

from itertools import chain, count
from tqdm import trange

def parse(raw, n):
    labels = list(map(int, raw)) 
    if n==10**6: labels += list(range(10, 10**6+1))
    labels.append(labels[0])
    nexts = [None] * len(labels)
    for a, b in zip(labels, labels[1:]): nexts[a] = b
    return labels[0], nexts

def prepare(curr, nexts):
    c, three = curr, []
    for _ in range(3):
        c = nexts[c]
        three.append(c)
    dest = curr - 1 or (len(nexts)-1)
    while dest in three:
        dest = dest - 1 or (len(nexts)-1)
    return three, dest

def play(raw, n):
    curr, nexts = parse(raw, n)
    for _ in (trange(n * 10) if n == 10**6 else range(n)):
        three, dest = prepare(curr, nexts)
        nexts[curr] = nexts[three[2]]
        nexts[three[2]] = nexts[dest]
        nexts[dest] = three[0]
        curr = nexts[curr]
    return nexts

def fst_star(raw, n=100): 
    nexts = play(raw, n)
    s, c = '', 1
    for _ in range(8):
        c = nexts[c]
        s += str(c)
    return s

def snd_star(raw):
    nexts = play(raw, 10**6)
    return str(nexts[1] * nexts[nexts[1]])

if __name__ == '__main__':
    assert fst_star('389125467', 10) == '92658374'
    # assert snd_star('389125467') == '149245887792'
    print(fst_star('789465123'))
    print(snd_star('789465123'))
