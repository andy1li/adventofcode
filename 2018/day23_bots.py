# https://adventofcode.com/2018/day/23

from typing import NamedTuple
import re

class Bot(NamedTuple): 
    x: int; y: int; z: int; r: int

    def __sub__(self, other):
        return ( abs(self.x-other.x)
               + abs(self.y-other.y)
               + abs(self.z-other.z))

def parse(input):
    return [
        Bot(*map(int, re.findall(r'-?\d+', line)))
        for line in input
    ]

def fst_star(bots):
    largest = max(bots, key=lambda bot: bot.r)
    return sum(
        largest-bot <= largest.r
        for bot in bots
    )

def count_in_range(bots, center):
    return sum(
        center-bot <= bot.r
        for bot in bots
    )

def snd_star(bots):
    candidates = [
        Bot(b.x-b.r/3, b.y-b.r/3, b.z-b.r/3, None)
        for b in bots
    ]
    most_in_range = max(candidates, key=lambda c: count_in_range(bots, c))
    return most_in_range - Bot(0, 0, 0, 0)

TEST = '''pos=<0,0,0>, r=4
pos=<1,0,0>, r=1
pos=<4,0,0>, r=3
pos=<0,2,0>, r=1
pos=<0,5,0>, r=3
pos=<0,0,3>, r=1
pos=<1,1,1>, r=1
pos=<1,1,2>, r=1
pos=<1,3,1>, r=1'''.split('\n')

if __name__ == '__main__':
    fst_star(parse(TEST)) == 7

    bots = parse(open('data/day23.in'))
    print(fst_star(bots))
    print(snd_star(bots))