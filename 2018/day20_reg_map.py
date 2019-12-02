# https://adventofcode.com/2018/day/20

from collections import defaultdict, deque
from typing import NamedTuple

class Pos(NamedTuple): 
    y: int; x: int

    def go(self, elta):
        D = {'N': Pos(1,  0), 'S': Pos(-1, 0),
             'W': Pos(0, -1), 'E': Pos( 0, 1)}
        return Pos(
            self.y + D[elta].y,
            self.x + D[elta].x
        )

def parse(regex):
    MAP = defaultdict(set)
    stack, curr = [], Pos(0, 0)
    for c in regex:
        if   c == '(': stack.append(curr)
        elif c == '|': curr = stack[-1]
        elif c == ')': curr = stack.pop()
        elif c in 'NSWE': 
            next = curr.go(c)
            MAP[curr].add(next)
            curr = next
    return MAP

def both_stars(MAP):
    q, seen = deque([(0, Pos(0, 0))]), set()
    fst, snd = 0, 0
    while q:
        depth, pos = q.popleft()
        
        fst = max(fst, depth)
        if depth >= 1000: snd += 1

        for next_pos in MAP[pos]:
            if next_pos in seen: continue
            seen.add(next_pos)
            q.append((depth+1, next_pos))

    return fst, snd

TEST1 = '^WNE$'
TEST2 = '^ENWWW(NEEE|SSE(EE|N))$'
TEST3 = '^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$'

if __name__ == '__main__':
    assert both_stars(parse(TEST1))[0] == 3
    assert both_stars(parse(TEST2))[0] == 10
    assert both_stars(parse(TEST3))[0] == 18

    print(both_stars(parse(open('data/day20.in').read())))