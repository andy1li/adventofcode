# https://adventofcode.com/2019/day/17

from intcode import run
from itertools import chain

def iterate(image):
    for y, row in enumerate(image):
        for x, val in enumerate(row):
             yield y, x, val

def get_neighbors(y, x):
    return [(y-1, x), (y, x+1), (y+1, x), (y, x-1)]

def within_bounds(image, y, x):
    height, width = len(image), len(image[0])
    return 0 <= y < height and 0 <= x < width

def get_val(image, pos):
    y, x = pos
    if within_bounds(image, y, x):
        return image[y][x]

def at_intersection(image, y, x, val):
    return val == '#' and all(
        within_bounds(image, ny, nx) and image[ny][nx] == '#'
        for ny, nx in get_neighbors(y, x)
    )

def sum_alignment(image):
    return sum( y * x 
        for y, x, val in iterate(image)
        if at_intersection(image, y, x, val)
    )

def generate_input(image, END=(26, 6)):
    pos = next( (y, x)
        for y, x, val in iterate(image)
        if val == '^'
    )
    assert pos == (40, 18) # start
    direction, path = 1, ['R', 0]

    while pos != END:
        neighbors = get_neighbors(*pos)
        next_pos = neighbors[direction]
        L, R = (direction-1)%4, (direction+1)%4
        nL, nR = neighbors[L], neighbors[R]

        if get_val(image, next_pos) == '#':
            path[-1] += 1
            pos = next_pos 
        elif get_val(image, nL) == '#':
            direction = L
            path.extend(['L', 0])
        elif get_val(image, nR) == '#':
            direction = R
            path.extend(['R', 0])

    assert path == ['R', 12, 'R', 4, 'R', 10, 'R', 12, 'R', 6, 'L', 8, 'R', 10, 'R', 12, 'R', 4, 'R', 10, 'R', 12, 'L', 8, 'R', 4, 'R', 4, 'R', 6, 'R', 12, 'R', 4, 'R', 10, 'R', 12, 'R', 6, 'L', 8, 'R', 10, 'L', 8, 'R', 4, 'R', 4, 'R', 6, 'R', 12, 'R', 4, 'R', 10, 'R', 12, 'R', 6, 'L', 8, 'R', 10, 'L', 8, 'R', 4, 'R', 4, 'R', 6]

    # for i, x in enumerate(path):
    #     print(x,  end='')
    #     if i%2: print(' ', end='')

    # A: R12 R4 R10 R12 
    # B: R6 L8 R10 
    # A: R12 R4 R10 R12 
    # C: L8 R4 R4 R6 
    # A: R12 R4 R10 R12 
    # B: R6 L8 R10 
    # C: L8 R4 R4 R6 
    # A: R12 R4 R10 R12 
    # B: R6 L8 R10 
    # C: L8 R4 R4 R6

    return '''A,B,A,C,A,B,C,A,B,C
R,12,R,4,R,10,R,12
R,6,L,8,R,10
L,8,R,4,R,4,R,6
n
'''

def get_image(code):
    computer = run(code, [])
    return ''.join(map(chr, computer)).strip().split('\n')

def count_dust(code, image):
    code[0] = 2
    computer = run(code, map(ord, generate_input(image)))
    for num in computer: print(chr(num), sep='', end='')
    return num

if __name__ == '__main__':
    code = [*map(int, open('data/day17.in').read().split(','))]
    image = get_image(code)
    print(sum_alignment(image), '\n')
    print(count_dust(code, image))