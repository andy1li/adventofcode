# https://adventofcode.com/2018/day/1

from itertools import accumulate, cycle

def fst_star(deltas): return sum(deltas)

def snd_star(deltas):
    seen = {0}
    for freq in accumulate(cycle(deltas)):
        if freq in seen: return freq
        seen.add(freq)

if __name__ == '__main__':
    deltas = [*map(int, open('data/day01.in'))]
    print(fst_star(deltas))
    print(snd_star(deltas))