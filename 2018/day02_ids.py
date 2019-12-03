# https://adventofcode.com/2018/day/2

from collections import Counter
from itertools   import combinations

def fst_star(ids): 
    two = three = 0
    for id in ids:
        times = set(Counter(id).values())
        if 2 in times: two += 1
        if 3 in times: three += 1
    return two * three

def snd_star(ids):
    for a, b in combinations(ids, 2):
        if sum(x!=y for x, y in zip(a, b)) == 1:
            return ''.join( x 
                for x, y in zip(a, b)
                if x == y
            ) 
            
if __name__ == '__main__':
    ids = [l.strip() for l in open('data/day02.in')]
    print(fst_star(ids))
    print(snd_star(ids))