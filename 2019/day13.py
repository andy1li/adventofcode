# https://adventofcode.com/2019/day/13

from intcode import run
from matplotlib import pyplot as plt
import numpy as np

cmp = lambda a, b: (a > b) - (a < b)
read = lambda g: (next(g), next(g), next(g))

def get_screen(game):
    screen = np.zeros([26, 40])
    for _ in range(26*40):
        x, y, t = read(game)
        screen[y, x] = t
    return screen

def count_blocks(code): 
    screen = get_screen(run(code, None))
    # plt.imshow(screen); plt.show()
    return (screen == 2).sum()

def play_game(code): 
    code[0], joystick = 2, [1]
    game = run(code, iter(joystick))
    screen = get_screen(game)

    while True:
        try: x, y, t = read(game) #; print(y, x, t)
        except StopIteration: break
        if x == -1: score = t; continue

        screen[y, x] = t
        if t == 3: paddle = x
        if t == 4: # ball = x
            joystick.append(cmp(x, paddle))
            # plt.imshow(screen); plt.show()
    print('score:', score)

if __name__ == '__main__':
    code = [*map(int, open('data/day13.in').read().split(','))]
    count_blocks(code)
    play_game(code)