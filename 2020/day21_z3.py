# https://adventofcode.com/2020/day/21

from z3 import *
from collections import defaultdict

def parse(raw):
    candidates, cnt = defaultdict(list), defaultdict(int)
    allergens, ingredients = set(), set()
    for line in raw:
        ings, alls = line.strip().split(' (contains ')
        ings = ings.split()
        ingredients |= set(ings)
        for a in alls.rstrip(')').split(', '):
            candidates[a] += set(ings),
            allergens.add(a)
        for i in ings: cnt[i] += 1

    candidates = {a: set.intersection(*m) for a, m in candidates.items()}
    return candidates, cnt, list(allergens), list(ingredients)

def solve(candidates, cnt, allergens, ingredients):
    s, Alls = Solver(), [Int(a) for a in allergens]
    for i, a in enumerate(allergens):
        s.add( Or([ Alls[i] == ingredients.index(c) for c in candidates[a]]) )
    s.add( Distinct(Alls) )
    s.check(); m = s.model()

    matched = { ingredients[m[a].as_long()]: str(a) for a in m }
    fst_star = sum(c for i, c in cnt.items() if i not in matched)
    snd_star = ','.join(sorted(matched, key=matched.get))
    return fst_star, snd_star

TEST = '''\
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)'''.splitlines()

if __name__ == '__main__':
    assert solve(*parse(TEST)) == (5, 'mxmxvkd,sqjhc,fvjkl')
    print(*solve(*parse(open('data/day21.in'))), sep='\n')

