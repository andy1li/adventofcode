# https://adventofcode.com/2021/day/13

from collections import namedtuple

DOT = namedtuple('DOT', 'x, y')

def parse_dots(raw):
    return set(DOT(*map(int, line.split(','))) for line in raw)

def fold(dot, axis, n):
    if axis == 'x' and dot.x < n or axis == 'y' and dot.y < n:
        return dot
    if axis == 'x': return DOT(n+(n-dot.x), dot.y)
    if axis == 'y': return DOT(dot.x, n+(n-dot.y))

def step(dots, axis, n):
    return set(fold(d, axis, n) for d in dots)

def show(dots):
    maxx, minx = max(d.x for d in dots), min(d.x for d in dots)
    maxy, miny = max(d.y for d in dots), min(d.y for d in dots)
    for y in range(miny, maxy+1):
        for x in range(minx, maxx+1):
            print('⬛️' if (x, y) in dots else '◻️', end='')
        print()
    print()

def fst_star(dots, folds): 
    return len(step(dots, *folds[0]))

def snd_star(dots, folds):
    for f in folds:
        dots = step(dots, *f)
    show(dots)

TEST = '''\
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0'''.splitlines()

if __name__ == '__main__':
    dots = parse_dots(TEST)
    folds = [('y', 7), ('x', 5)]
    assert fst_star(dots, folds) == 17
    snd_star(dots, folds)

    dots = parse_dots(open('data/day13.in'))
    folds = [
        ('x', 655), ('y', 447), ('x', 327), ('y', 223), 
        ('x', 163), ('y', 111), ('x', 81), ('y', 55), 
        ('x', 40), ('y', 27), ('y', 13), ('y', 6)
    ]
    print(fst_star(dots, folds))
    snd_star(dots, folds)