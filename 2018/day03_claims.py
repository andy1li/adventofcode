# https://adventofcode.com/2018/day/3

from collections import Counter
import re 

def parse_claim(line): 
    claim = re.match(r'#\d+ @ (\d+),(\d+): (\d+)x(\d+)', line)
    return [int(x) for x in claim.groups()]

def apply_claims(claims): 
    return Counter(
        (x+i, y+j)
        for x, y, w, h in claims
        for i in range(w)
        for j in range(h)
    )

def fst_star(fabric): return sum(v>1 for v in fabric.values())

def snd_star(fabric, claims): 
    for i, (x, y, w, h) in enumerate(claims, start=1):
        if all(
            fabric[x+i, y+j] == 1
            for i in range(w)
            for j in range(h)
        ): return i

if __name__ == '__main__':
    claims = [*map(parse_claim, open('data/day03.in'))]
    fabric = apply_claims(claims)
    print(fst_star(fabric))
    print(snd_star(fabric, claims))