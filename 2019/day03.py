# https://adventofcode.com/2019/day/3

from collections import defaultdict

DELTA = {
    'U': (0, 1), 'D': (0, -1),
    'R': (1, 0), 'L': (-1, 0)
}

def parse(input): 
    return [line.split(',') for line in input]

def walk(wire):
    i = x = y = 0
    for section in wire:
        direction, steps = section[0], int(section[1:])
        dx, dy = DELTA[direction]
        for _ in range(steps):
            i += 1; x += dx; y += dy
            yield i, x, y

def fst_path(wires):
    grid = defaultdict(int)
    for i, x, y in walk(wires[0]):
        if not grid[x, y]: grid[x, y] = i
    return grid

def fst_star(wires): 
    grid = fst_path(wires)
    return min( abs(x) + abs(y)
        for i, x, y in walk(wires[1])
        if grid[x, y]
    )

def snd_star(wires): 
    grid = fst_path(wires)
    return min( grid[x, y] + i
        for i, x, y in walk(wires[1])
        if grid[x, y]
    )


TEST1 = '''R8,U5,L5,D3
U7,R6,D4,L4'''.split('\n')
TEST2 = '''R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83'''.split('\n')
TEST3 = '''R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'''.split('\n')

if __name__ == '__main__':
    assert fst_star(parse(TEST1)) == 6
    assert fst_star(parse(TEST2)) == 159
    assert fst_star(parse(TEST3)) == 135

    assert snd_star(parse(TEST1)) == 30
    assert snd_star(parse(TEST2)) == 610
    assert snd_star(parse(TEST3)) == 410

    wires = parse(open('data/day03.in'))
    print(fst_star(wires))
    print(snd_star(wires))
