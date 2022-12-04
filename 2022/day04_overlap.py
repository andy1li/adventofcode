# https://adventofcode.com/2022/day/4

from collections import namedtuple
from typing import List, Tuple

Segment = namedtuple('Segment', 'lo hi')
Segments = Tuple[Segment, Segment]

def parse_pairs(raw) -> List[Segments]:
    def parse_segment(raw_segment: List[str]):
        return Segment(*map(int, raw_segment))

    def parse_pair(raw_pair: List[str]):
        a, b = raw_pair
        return parse_segment(a.split('-')), parse_segment(b.split('-'))

    return [parse_pair(line.split(',')) for line in raw]

def contain(pair: Segments) -> bool:
    a, b = pair
    return (
        a.lo <= b.lo and b.hi <= a.hi
     or b.lo <= a.lo and a.hi <= b.hi
    )  

def overlap(pair: Segments) -> bool:
    a, b = pair
    return (
        a.lo <= b.lo <= a.hi 
     or a.lo <= b.hi <= a.hi
     or b.lo <= a.lo <= b.hi 
     or b.lo <= a.hi <= b.hi 
    )

def fst_star(pairs: List[Segments]): 
    return sum(map(contain, pairs))

def snd_star(pairs: List[Segments]):
    return sum(map(overlap, pairs))

TEST = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''.splitlines()

if __name__ == '__main__':
    pairs = parse_pairs(TEST)
    assert fst_star(pairs) == 2
    assert snd_star(pairs) == 4

    pairs = parse_pairs(open('data/day04.in').read().splitlines())
    print(fst_star(pairs))
    print(snd_star(pairs))