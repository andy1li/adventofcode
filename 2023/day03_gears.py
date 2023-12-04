# https://adventofcode.com/2023/day/3

from collections import defaultdict
from math import prod
import re

def scan(grid, row, start, end):
    nrows, ncols = len(grid), len(grid[row])
    yield from ( (i, j)
        for i in range(max(0, row-1), min(nrows, row+2))
        for j in range(max(0, start-1), min(ncols, end+2))
    )

def check_part(grid, row, start, end):
    return any(
        not grid[i][j].isdigit() and grid[i][j] != '.'
        for i, j in scan(grid, row, start, end)
    )

def find_star(grid, row, start, end):
    return next(( (i, j) 
        for i, j in scan(grid, row, start, end) 
        if grid[i][j] == '*'
    ), None)

def parse(grid):
    return [
        (int(n.group()), find_star(grid, i, n.start(), n.end()-1))
        for i, row in enumerate(grid)
        for n in re.finditer(r'\d+', row)
        if check_part(grid, i, n.start(), n.end()-1)
    ]
    
def fst_star(parts):
    return sum(p[0] for p in parts)

def find_gears(parts):
    stars = defaultdict(list)
    for number, star in parts:
        if star: stars[star].append(number)
    return ( numbers
        for numbers in stars.values()
        if len(numbers) == 2
    )

def snd_star(parts):
    gears = find_gears(parts)
    return sum(map(prod, gears))
    

TEST = '''\
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''.splitlines()

if __name__ == '__main__':
    parts = parse(TEST)
    assert fst_star(parts) == 4361
    assert snd_star(parts) == 467835
    
    parts = parse(open('data/day03.in').read().splitlines())
    print(fst_star(parts))
    print(snd_star(parts))
