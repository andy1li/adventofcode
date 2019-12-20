# https://adventofcode.com/2019/day/17

from advent import get_neighbors, get_neighbor_items, iterate, within_bounds
from intcode import run

def get_value(image, pos):
    y, x = pos
    if within_bounds(image, y, x):
        return image[y][x]

def at_intersection(image, y, x, value):
    return value == '#' and all( nval == '#'
        for _, nval in get_neighbor_items(image, y, x)
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

        if get_value(image, next_pos) == '#':
            path[-1] += 1
            pos = next_pos 
        elif get_value(image, nL) == '#':
            direction = L
            path.extend(['L', 0])
        elif get_value(image, nR) == '#':
            direction = R
            path.extend(['R', 0])

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
'''.encode()

def get_image(code):
    computer = run(code, [])
    output = bytes(computer).decode()
    return output.strip().split()

def sum_alignment(image):
    return sum( y * x 
        for y, x, val in iterate(image)
        if at_intersection(image, y, x, val)
    )

def collect_dust(code, image):
    code[0] = 2
    computer = run(code, generate_input(image))
    output = list(computer); dust = output.pop()
    print(bytes(output).decode())
    return dust

if __name__ == '__main__':
    code = [*map(int, open('data/day17.in').read().split(','))]
    image = get_image(code)
    print(sum_alignment(image))
    print(collect_dust(code, image))