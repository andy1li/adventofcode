# https://adventofcode.com/2019/day/4

from collections import Counter 

def increasing(n):
    return all(a <= b for a, b in zip(n, n[1:]))

def adjacent(n):
    return any(a == b for a, b in zip(n, n[1:]))

def twice_only(n):
    return any(c == 2 for c in Counter(n).values())
    
def fst_star(candidates):
    return sum(
        increasing(n) and adjacent(n)
        for n in candidates
    )

def snd_star(candidates): 
    return sum(
        increasing(n) and twice_only(n)
        for n in candidates
    )

if __name__ == '__main__':
    CANDIDATES = [*map(str, range(178416, 676461+1))]
    print(fst_star(CANDIDATES))
    print(snd_star(CANDIDATES))