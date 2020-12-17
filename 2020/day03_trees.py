# https://adventofcode.com/2020/day/3

from math import prod

def slide(n, m, right, down):
    r = c = 0
    while r < n-down:
        r += down
        c = (c + right) % m
        yield r, c 

def count_tree(grid, right=3, down=1): 
    n, m = len(grid), len(grid[0])
    return sum(grid[r][c]=='#' for r, c in slide(n, m, right, down))

def check_angles(grid):
    angles = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    return prod( count_tree(grid, right, down) for right, down in angles )

TEST = '''\
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#'''.split()

if __name__ == '__main__':
    assert count_tree(TEST) == 7
    assert check_angles(TEST) == 336
    grid = open('data/day03.in').readlines()
    print(count_tree(grid))
    print(check_angles(grid))
