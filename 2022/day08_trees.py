# https://adventofcode.com/2022/day/8

from advent import iterate
from math import prod

def parse_grid(raw):
    return [[*map(int, line.strip())] for line in raw]

def fst_star(grid): 
    visible, n, maxh = set(), len(grid), -1

    def test(y, x):
        nonlocal maxh
        if grid[y][x] > maxh:
            visible.add((y, x))
            maxh = grid[y][x]

    for y in range(n):
        maxh = -1
        for x in range(n): test(y, x)
        maxh = -1
        for x in reversed(range(n)): test(y, x)

    for x in range(n):
        maxh = -1
        for y in range(n): test(y, x)
        maxh = -1
        for y in reversed(range(n)): test(y, x)
                
    return len(visible)
             
def snd_star(grid):
    n = len(grid)

    def score(triple):
        y, x, val = triple

        rgt = (grid[y][i] for i in range(x+1, n))
        lft = (grid[y][i] for i in range(x-1, -1, -1))
        up  = (grid[i][x] for i in range(y-1, -1, -1))
        dwn = (grid[i][x] for i in range(y+1, n))
        
        def look(direction):
            view = 0
            for h in direction:
                view += 1
                if h >= val: return view
            return view

        return prod(map(look, [lft, rgt, up, dwn]))

    return max(map(score, iterate(grid)))

TEST = '''\
30373
25512
65332
33549
35390'''.splitlines()

if __name__ == '__main__':
    grid = parse_grid(TEST)
    assert fst_star(grid) == 21
    assert snd_star(grid) == 8

    grid = parse_grid(open('data/day08.in'))
    print(fst_star(grid))
    print(snd_star(grid))