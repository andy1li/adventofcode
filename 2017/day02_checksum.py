# https://adventofcode.com/2017/day/2

from itertools import combinations

def parse(raw):
    return [list(map(int, line.split())) for line in raw]

def max_min(row):
    return max(row) - min(row)

def divisible(row):
    for a, b in combinations(row, 2):
        if a/b == a//b: return a//b
        if b/a == b//a: return b//a

def checksum(grid, func=max_min):
    return sum(map(func, grid))

TEST1 = '''5 1 9 5
7 5 3
2 4 6 8'''.splitlines()
TEST2 = '''5 9 2 8
9 4 7 3
3 8 6 5'''.splitlines()

if __name__ == '__main__':
    assert checksum(parse(TEST1)) == 18
    assert checksum(parse(TEST2), divisible) == 9

    grid = parse(open('data/day02.in'))
    print(checksum(grid))
    print(checksum(grid, divisible))