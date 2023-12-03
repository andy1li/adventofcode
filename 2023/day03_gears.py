# https://adventofcode.com/2023/day/3

from collections import defaultdict
from math import prod

def scan(grid, row, start, end):
    nrows, ncols = len(grid), len(grid[row])
    yield from ( (i, j)
        for i in range(max(0, row-1), min(nrows, row+2))
        for j in range(max(0, start-1), min(ncols, end+2))
    )

def check_part_number(grid, row, start, end):
    return any(
        not grid[i][j].isdigit() and grid[i][j] != '.'
        for i, j in scan(grid, row, start, end)
    )

def find_star(grid, row, start, end):
    return next( ((i, j) 
        for i, j in scan(grid, row, start, end) 
        if grid[i][j] == '*'
    ), None)

def parse(grid):
    for i, row in enumerate(grid):
        start = None
        for j, x in enumerate(row):
            if x.isdigit() and start is None: 
                start = j
            if not x.isdigit() and j-1 >= 0 and row[j-1].isdigit():
                if check_part_number(grid, i, start, j-1):
                    yield int(row[start:j]), find_star(grid, i, start, j-1)
                start = None

        if start is not None and check_part_number(grid, i, start, j):
            yield int(row[start:]), find_star(grid, i, start, j)

def fst_star(parts):
    return sum(p[0] for p in parts)

def find_gears(parts):
    stars = defaultdict(list)
    for number, star in parts:
        if star is not None:
            stars[star].append(number)
    return ( numbers
        for star, numbers in stars.items()
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
    parts = list(parse(TEST))
    assert fst_star(parts) == 4361
    assert snd_star(parts) == 467835
    
    parts = list(parse(open('data/day03.in').read().splitlines()))
    print(fst_star(parts))
    print(snd_star(parts))
