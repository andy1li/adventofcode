# https://adventofcode.com/2019/day/13

from intcode import run
from matplotlib.animation import FuncAnimation
from matplotlib import pyplot as plt
import numpy as np

cmp = lambda a, b: (a > b) - (a < b)
read = lambda g: (next(g), next(g), next(g))

def init_image(game, width=26, height=40):
    image = np.zeros([width, height], dtype=int)
    for _ in range(width * height):
        x, y, t = read(game)
        image[y, x] = t
    return image

def count_blocks(code): 
    image = init_image(run(code, []))
    # plt.imshow(image); plt.show()
    return (image == 2).sum()

def play_game(code, animate=False): 
    code[0], joystick = 2, [1]
    game = run(code, joystick)
    image = init_image(game)
    screen = plt.imshow(image)
    
    def step(_):
        global score, paddle
        x, y, t = read(game)
        image[y, x] = t
        if x == -1: score = t
        if t == 3: paddle = x
        if t == 4: # ball = x
            joystick.append(cmp(x, paddle))
            screen.set_data(image)
        return screen

    try:
        _ = FuncAnimation(plt.gcf(), step, interval=1)
        if animate: plt.show()
        while True: step(None)

    except StopIteration:
        global score
        print('score:', score)

if __name__ == '__main__':
    code = [*map(int, open('data/day13.in').read().split(','))]
    print(count_blocks(code))
    play_game(code, animate=True)