# https://adventofcode.com/2021/day/17

from collections import namedtuple
import numpy as np

class Target(namedtuple('Target', 'x_lo, x_hi, y_lo, y_hi')):
    def hit(self, pos):
        x, y = pos
        return (self.x_lo <= x <= self.x_hi 
            and self.y_lo <= y <= self.y_hi
        )

    def miss(self, pos):
        x, y = pos
        return x > self.x_hi or y < self.y_lo

class Trajectory:
    def __init__(self, target, velocity):
        self.velocity = velocity
        self.pos = np.array([0, 0])
        self.max_y = -float('inf')
        self.hit = False
        while not target.miss(self.pos):
            self.step()

    def step(self):
        self.pos += self.velocity
        vx, vy = self.velocity            
        self.velocity = np.array([
            vx and vx-vx//abs(vx), vy-1
        ])
        self.max_y = max(self.max_y, self.pos[1])
        self.hit = self.hit or target.hit(self.pos)

def fst_star(target, x_hi=200, y_hi=200):
    ans = -float('inf')
    for x in range(1, x_hi):
        for y in range(target.y_lo, y_hi):
            t = Trajectory(target, np.array([x, y]))
            if t.hit: ans = max(ans, t.max_y)
    return ans

def snd_star(target, x_hi=300, y_hi=300):
    ans = 0
    for x in range(1, x_hi):
        for y in range(target.y_lo, y_hi):
            t = Trajectory(target, np.array([x, y]))
            if t.hit: ans += 1
    return ans

if __name__ == '__main__':
    target = Target(20, 30, -10, -5)
    assert fst_star(target) == 45
    assert snd_star(target) == 112

    target = Target(217, 240, -126, -69)
    print(fst_star(target))
    print(snd_star(target))
