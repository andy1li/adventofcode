# https://adventofcode.com/2019/day/24

from advent import get_neighbors
from collections import Counter, defaultdict

def parse(input):
    levels = defaultdict(set)
    for y, row in enumerate(input):
        for x, val in enumerate(row.strip()):
            if val == '#': levels[0].add((y, x))
    return levels

def show(level):
    return '\n'.join(
        ''.join('#' if (y, x) in level else '.' for x in range(5))
        for y in range(5)
    ) + '\n'

def normal_neighbors(y, x):
    for ny, nx in get_neighbors(y, x):
        if 0 <= ny < 5 and 0 <= nx < 5:
            yield 0, ny, nx

def recursive_neighbors(y, x):
    for ny, nx in get_neighbors(y, x):
        if   ny < 0: yield -1, 1, 2 # top
        elif ny > 4: yield -1, 3, 2 # bottom
        elif nx < 0: yield -1, 2, 1 # left
        elif nx > 4: yield -1, 2, 3 # right

        elif (ny, nx) == (2, 2):
            if   y == 1: yield from ((1, 0, x) for x in range(5))
            elif y == 3: yield from ((1, 4, x) for x in range(5))
            elif x == 1: yield from ((1, y, 0) for y in range(5))
            elif x == 3: yield from ((1, y, 4) for y in range(5))

        else: yield 0, ny, nx

def step(levels, get_neighbors):
    new_levels, seen = defaultdict(set), set()

    def apply_rule(l, y, x, neighbors, has_bug):
        cnt = Counter(
            (ny, nx) in levels[l+dl]
            for dl, ny, nx in neighbors
        )
        if has_bug and cnt[True] == 1: 
            new_levels[l].add((y, x))
        elif not has_bug and cnt[True] in [1, 2]:
            new_levels[l].add((y, x))

    def dfs(l, y, x):
        if (l, y, x) in seen: return
        seen.add((l, y, x))

        neighbors = list(get_neighbors(y, x))
        has_bug = (y, x) in levels[l]
        apply_rule(l, y, x, neighbors, has_bug)

        if has_bug: 
            for dl, ny, nx in neighbors: dfs(l+dl, ny, nx)

    for l, level in levels.copy().items():
        for y, x in level:
            dfs(l, y, x)

    return new_levels
            
def find_repetition(levels):
    seen = { show(levels[0]) }
    while True:
        levels = step(levels, normal_neighbors)
        level = show(levels[0])
        if level in seen: return levels[0]
        seen.add(level)

def score(level): 
    return sum( 
        1 << (y * 5 + x)
        for y, x in level
    )

def repeat(levels, n):
    for _ in range(n):
        levels = step(levels, recursive_neighbors)
    return sum(map(len, levels.values()))

TEST = '''....#
#..#.
#..##
..#..
#....'''.split()

if __name__ == '__main__':
    levels = parse(TEST)
    assert score(find_repetition(levels)) == 2129920
    
    levels = parse(open('data/day24.in').readlines())
    print(score(find_repetition(levels)))
    print(repeat(levels, 200))
