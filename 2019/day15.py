# https://adventofcode.com/2019/day/15

from enum       import Enum
from intcode    import run
from matplotlib import pyplot as plt
from typing     import NamedTuple
import numpy as np
import pickle

class Status(Enum): WALL, ROOM, OXYGEN = range(3)

class Move(Enum): 
    NORTH, SOUTH, WEST, EAST = range(1, 5)

    @staticmethod
    def parse(a, b):
        ay, ax = a; by, bx = b
        if by - ay == -1: return Move.NORTH
        if by - ay ==  1: return Move.SOUTH
        if bx - ax == -1: return Move.WEST
        if bx - ax ==  1: return Move.EAST
 
def neighbors(y, x):
    return [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]

OFFSET = 22
class Bot():
    def __init__(self, code):
        self.remote = []
        self.game = run(code, iter(self.remote))

        self.pos = 0, 0
        self.rooms = set([self.pos])
        self.unknowns = set(neighbors(*self.pos))
        self.walls = set()
        self.maze = np.zeros([OFFSET*2-1, OFFSET*2-1])

        self.explore()

    def visualize(self):
        for y, x in self.rooms:    self.maze[y+OFFSET, x+OFFSET] = 1
        for y, x in self.unknowns: self.maze[y+OFFSET, x+OFFSET] = 2
        for y, x in self.walls:    self.maze[y+OFFSET, x+OFFSET] = 10
        self.maze[self.pos[0]+OFFSET, self.pos[1]+OFFSET] = 15
        plt.imshow(self.maze); plt.show()

    def bfs(self, start, targets):
        q, p, seen = [start], {}, set()
        for pos in q:
            if pos in targets:
                path = [Move.parse(p[pos], pos)]
                while p[pos] != start:
                    pos = p[pos]
                    path.append(Move.parse(p[pos], pos))
                return list(reversed(path))

            for next_pos in neighbors(*pos):
                if (next_pos in seen or next_pos in self.walls): continue
                seen.add(next_pos)
                p[next_pos] = pos
                q.append(next_pos)

    def execute(self, plan):
        for move in plan:
            command = move.value

            pos = neighbors(*self.pos)[command-1]
            self.remote.append(command)
            status = Status(next(self.game))
            self.unknowns.discard(pos)

            if status == Status.WALL: 
                self.walls.add(pos)
            else:
                self.rooms.add(pos)
                self.pos = pos
                self.unknowns |= (
                    set(neighbors(*pos))
                  - self.walls - self.rooms
                )
                if status == Status.OXYGEN: self.oxygen = pos
                
    def explore(self):
        while self.unknowns:
            plan = self.bfs(self.pos, self.unknowns) 
            self.execute(plan)

def oxygen_distance(bot):
    return len(bot.bfs([0, 0], [bot.oxygen]))

def oxygen_time(bot): 
    return max(
        len(bot.bfs(bot.oxygen, [room]))
        for room in bot.rooms
        if room != bot.oxygen
    )

if __name__ == '__main__':
    code = [*map(int, open('data/day15.in').read().split(','))]
    bot = Bot(code)
    bot.visualize()
    print(oxygen_distance(bot))
    print(oxygen_time(bot))