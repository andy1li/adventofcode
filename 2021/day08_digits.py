# https://adventofcode.com/2021/day/8

from z3 import *
from itertools import product, permutations

def parse(raw):
    entries = []
    for line in raw:
        patterns, four = line.split(' | ')
        patterns = set(frozenset(p) for p in patterns.split())
        four = four.split()
        entries.append( (patterns, four) )
    return entries 

def fst_star(entries): 
    return sum(
        len(digit) in (2, 3, 4, 7)
        for patterns, four in entries
        for digit in four
    )

SEVEN, MAP = 'abcdefg', [
    frozenset('abcefg'), 
    frozenset('cf'), frozenset('acdeg'), frozenset('acdfg'), 
    frozenset('bcdf'), frozenset('abdfg'), frozenset('abdefg'), 
    frozenset('acf'), frozenset('abcdefg'), frozenset('abcdfg')
]

def check(set_pattern, perm):
    back = dict(zip(SEVEN, perm))
    candidate = set( frozenset(back[x] for x in seg) for seg in MAP )
    # print(candidate, set_pattern)
    return candidate == set_pattern

def snd_star(entries):
    ans = 0
    for patterns, four in entries:
        perm = next( perm
            for perm in permutations(SEVEN)
            if check(patterns, perm)
        )
        wires = dict(zip(perm, SEVEN))
        ans += int(''.join(
            str(MAP.index(set(wires[x] for x in digit)))
            for digit in four
        ))
    return ans

TEST = '''\
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce'''.splitlines()

if __name__ == '__main__':
    assert fst_star(parse(TEST)) == 26
    assert snd_star(parse(TEST)) == 61229

    entries = parse(open('data/day08.in'))
    print(fst_star(entries))
    print(snd_star(entries))