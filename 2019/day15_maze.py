# https://adventofcode.com/2019/day/15

from enum import Enum
from intcode import run
from matplotlib import pyplot as plt
import numpy as np

class Move(Enum): 
    NORTH, SOUTH, WEST, EAST = range(1, 5)

    @staticmethod
    def parse(a, b):
        direction = get_neighbors(*a).index(b)
        return Move(direction+1)
 
def get_neighbors(y, x):
    return [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]

def get_moves(start, p, pos):
    moves = [ Move.parse(p[pos], pos) ]
    while p[pos] != start:
        pos = p[pos]
        moves.append( Move.parse(p[pos], pos) )
    return list(reversed(moves))

OFFSET = 22
class Bot():
    def __init__(self, code):
        self.remote = []
        self.game = run(code, self.remote)

        self.pos = 0, 0
        self.rooms = {self.pos}
        self.unknowns = set(get_neighbors(*self.pos))
        self.walls = set()
        self.maze = np.zeros([OFFSET*2-1, OFFSET*2-1], dtype=int)

        self.explore()

    def visualize(self):
        for y, x in self.rooms:    self.maze[y+OFFSET, x+OFFSET] = 1
        for y, x in self.unknowns: self.maze[y+OFFSET, x+OFFSET] = 2
        for y, x in self.walls:    self.maze[y+OFFSET, x+OFFSET] = 10
        self.maze[self.oxygen[0]+OFFSET, self.oxygen[1]+OFFSET] = 15
        plt.imshow(self.maze); plt.show()

    def bfs(self, start, targets):
        q, p, seen = [start], {}, set()
        for pos in q:
            if pos in targets: return get_moves(start, p, pos)
            for neighbor in get_neighbors(*pos):
                if (neighbor in seen or neighbor in self.walls): continue
                seen.add(neighbor)
                p[neighbor] = pos
                q.append(neighbor)

    def resolve(self, pos, moved):
        self.unknowns.discard(pos)
        if not moved: 
            self.walls.add(pos)
        else:
            self.rooms.add(pos)
            self.pos = pos
            self.unknowns |= (
                set(get_neighbors(*pos)) - self.walls - self.rooms
            )
            if moved == 2: self.oxygen = pos

    def execute(self, moves):
        for move in moves:
            command = move.value
            pos = get_neighbors(*self.pos)[command-1]
            self.remote.append(command)
            self.resolve(pos, next(self.game))
            
    def explore(self):
        while self.unknowns:
            moves = self.bfs(self.pos, self.unknowns) 
            self.execute(moves)

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