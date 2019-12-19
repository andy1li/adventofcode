# https://adventofcode.com/2018/day/18

from collections import Counter, defaultdict
from itertools import count, product
from tqdm import tqdm

def parse(input):
    area = defaultdict(str)
    for y, row in enumerate(input):
        for x, cell in enumerate(row.strip()):
            area[y, x] = cell
    return area

def step(area, size=50):
    new_area = defaultdict(str)
    for y, x in product(range(size), repeat=2):
        cnt = Counter(
            area[y+dy, x+dx] for dy, dx in [
                (-1, -1), (-1, 0), (-1, 1),
                ( 0, -1),          ( 0, 1),
                ( 1, -1), ( 1, 0), ( 1, 1)
        ])
        if area[y, x] == '.':
            new_area[y, x] = '|' if cnt['|'] >= 3 else '.'
        if area[y, x] == '|':
            new_area[y, x] = '#' if cnt['#'] >= 3 else '|'
        if area[y, x] == '#':
            new_area[y, x] = '#' if cnt['#']>=1 and cnt['|']>=1 else '.'
    return new_area

def show(area, size=50):
    return '\n'.join(
        ''.join(area[y, x] for x in range(size))
        for y in range(size)
    ) + '\n'

def fst_star(area, size=50):
    for i in range(10):
        area = step(area, size)
        # print(f'After {i+1} minute:')
        # print(show(area, size))
    cnt = Counter(area.values())
    return cnt['|'] * cnt['#']

def snd_star(area, end=1000000000):
    areas, resources, t = {}, [], tqdm()
    for i in count():
        cnt = Counter(area.values()); t.update()
        resources.append(cnt['|'] * cnt['#'])

        area = step(area); a = show(area)
        if a in areas:
            zero = areas[a]; mod = i-zero; t.close()
            n = zero + (1000000000-zero)%mod
            return resources[n]
        areas[a] = i

TEST = '''.#.#...|#.
.....#|##|
.|..|...#.
..|#.....#
#.#|||#|#|
...#.||...
.|....|...
||...#|.#|
|.||||..|.
...#.|..|.'''.split()

if __name__ == '__main__':
    assert fst_star(parse(TEST), 10) == 1147

    grid = parse(open('data/day18.in'))
    print(fst_star(grid))
    print(snd_star(grid))

