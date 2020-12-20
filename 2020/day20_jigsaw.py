# https://adventofcode.com/2020/day/20

from collections import defaultdict
from pprint import pformat 
from matplotlib import pyplot as plt
import numpy as np

key = lambda b: min([b, b[::-1]])

class Tile:
    def __init__(self, id, grid):
        self.id = id 
        self.grid = grid

    def top(self): return self.grid[0]
    def right(self): return ''.join(row[-1] for row in self.grid)
    def bottom(self): return self.grid[-1]
    def left(self): return ''.join(row[0] for row in self.grid)
    def __repr__(self): return str(self.id)

    def __iter__(self): 
        return iter([self.top(), self.right(), self.bottom(), self.left()])
    
    def rotate(self): self.grid = [''.join(row[::-1]) for row in zip(*self.grid)]
    def flip(self): self.grid = [''.join(row[::-1]) for row in self.grid]        

    def align(self, border, side):
        for _ in range(2):
            for _ in range(4):
                self_side = getattr(self, side)()
                if self_side == border: return
                self.rotate()
            self.flip()

    def to_image(self, crop=True):
        start, end = (1, -1) if crop else (0, len(self.grid[0]))
        return np.array([
            [(x=='#') * 255 for x in row[start:end]] 
            for row in self.grid[start:end]
        ], np.uint8)
    
class Snowball(Tile):
    def __init__(self, tile): self.grid = [[tile]]
    def __repr__(self): return pformat(self.grid)

    def rotate(self):
        self.grid = [row[::-1] for row in zip(*self.grid)]
        for row in self.grid:
            for tile in row: tile.rotate()

    def is_ready(self, agg):
        bottom_left = self.bottom()[0]
        border_key = key(bottom_left.bottom())
        return len(agg.get(border_key, [])) > 1

    def prepare(self, agg): 
        while not self.is_ready(agg): self.rotate()

    def roll_on(self, new_bottom):
        assert len(self.bottom()) == len(new_bottom)
        self.grid.append(new_bottom)
        self.rotate()

    def to_image(self):
        return np.vstack([
            np.hstack([x.to_image() for x in row]) 
            for row in self.grid
        ])

    def step(self, inners, agg):
        self.prepare(agg) 
        new_bottom = []
        for sb_tile in self.bottom():
            common_border = sb_tile.bottom()
            common_key = key(common_border)

            nb_tile = (agg[common_key] - {sb_tile}).pop()
            nb_tile.align(common_border, 'top')
            new_bottom.append(nb_tile)

            inners.discard(nb_tile)
            agg[common_key].discard(sb_tile)
            agg[common_key].discard(nb_tile)

        self.roll_on(new_bottom)
        return inners, agg

def parse(raw):
    def parse_tile(raw):
        grid = raw.splitlines()
        id = int(grid.pop(0)[5:-1])
        return Tile(id, grid)
    return {parse_tile(r) for r in raw.split('\n\n')}

def peel(tiles):
    agg = defaultdict(set)
    for tile in tiles:
        for border in tile:
            agg[key(border)].add(tile)
    
    outer_borders, inner_borders = set(), set()
    for border, ts in agg.items():
        if len(ts) == 1: outer_borders.add(key(border))
        elif len(ts) == 2: inner_borders.add(key(border))
        else: raise ValueError
    outer_tiles = {t for t in tiles if any(key(b) in outer_borders for b in t)}
    inner_tiles = {t for t in tiles if all(key(b) in inner_borders for b in t)}
    return outer_tiles, agg, inner_tiles

def all_layers(tiles):
    layers, inners = [], tiles
    while inners:
        outers, agg, inners = peel(inners) 
        layers.append([outers, agg])
    return layers

def reassemble(tiles):
    layers = all_layers(tiles)
    inners, agg = layers.pop()
    snowball = Snowball(inners.pop())
    while layers:
        if not inners: inners, agg = layers.pop()
        while inners: inners, agg = snowball.step(inners, agg)
    return snowball

def fst_star(snowball):
    return snowball.top()[0].id * snowball.top()[-1].id * snowball.bottom()[0].id * snowball.bottom()[-1].id

monster = '''\
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''.splitlines()
monster = Tile(0, monster).to_image(crop=False)

test = '''\
.####...#####..#...###..
#####..#..#.#.####..#.#.
.#.#...#.###...#.##.##..
#.#.##.###.#.##.##.#####
..##.###.####..#.####.##
...#.#..##.##...#..#..##
#.##.#..#.#..#..##.#.#..
.###.##.....#...###.#...
#.####.#.#....##.#..#.#.
##...#..#....#..#...####
..#.##...###..#.#####..#
....#.##.#.#####....#...
..##.##.###.....#.##..#.
#...#...###..####....##.
.#.##...#.##.#.#.###...#
#.###.#..####...##..#...
#.###...#.##...#.######.
.###.###.#######..#####.
..##.#..#..#.#######.###
#.#..##.########..#..##.
#.#####..#.#...##..#....
#....##..#.#########..##
#...#.....#..##...###.##
#..###....##.#...##.##.#'''.splitlines()
test = Tile(0, test).to_image(crop=False)

def snd_star(image):
    plt.imshow(image)
    plt.show()

# snd_star(test)

if __name__ == '__main__':
    snowball = reassemble(parse(open('data/day20_test.in').read()))
    assert fst_star(snowball) == 20899048083289
    snowball = reassemble(parse(open('data/day20.in').read()))
    print(fst_star(snowball))

    # snowball = snowball.to_image()
    # for _ in range(2):
    #     for _ in range(4):
    #         foo(snowball)
    #         snowball = np.rot90(snowball)
    #     snowball = np.flip(snowball)
