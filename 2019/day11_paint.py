# https://adventofcode.com/2019/day/11

from collections import defaultdict
from enum        import Enum
from intcode     import run
from matplotlib  import pyplot as plt
from typing      import NamedTuple

DELTA = [(-1, 0), (0, 1), (1, 0), (0, -1)]

class Direction(Enum): 
    UP, RIGHT, DOWN, LEFT = range(4)

class Pos(NamedTuple):
    y: int; x: int; direction: int

    def step(self, turn):
        y, x, direction = self
        if not turn: turn = -1
        direction = (direction.value + turn) % 4
        dy, dx = DELTA[direction]
        return Pos(y+dy, x+dx, Direction(direction))

def visualize(hull):
    min_x = min(p[1] for p in hull)
    min_y = min(p[0] for p in hull)
    max_x = max(p[1] for p in hull)
    max_y = max(p[0] for p in hull)

    image = [ 
        [hull[y-min_y, x-min_x] for x in range(min_x, max_x+1)]
        for y in range(min_y, max_y+1)
    ]
    plt.imshow(image); plt.show()

def run_robot(code, start=0): 
    pos = Pos(0, 0, Direction.UP)
    camera, hull = [start], defaultdict(int)
    computer = run(code, camera)
    while True:
        try:
            hull[pos.y, pos.x] = next(computer)
            pos = pos.step(next(computer))
            camera.append(hull[pos.y, pos.x])
        except StopIteration: 
            return hull

if __name__ == '__main__':
    code = [*map(int, open('data/day11.in').read().split(','))]
    print(len(run_robot(code)))
    visualize(run_robot(code, 1))