# https://adventofcode.com/2020/day/20

from advent import iterate
from collections import defaultdict
from itertools import chain
from pprint import pformat 
from matplotlib import pyplot as plt
import numpy as np

key = lambda b: min([b, b[::-1]])
to_dots = lambda grid: { (y, x) for y, x, v in iterate(grid) if v == 255 }

class Tile:
    def __init__(self, id, grid):
        self.id = id 
        self.grid = grid

    def top(self): return tuple(self.grid[0])
    def right(self): return tuple(row[-1] for row in self.grid)
    def bottom(self): return tuple(self.grid[-1])
    def left(self): return tuple(row[0] for row in self.grid)
    def __repr__(self): return str(self.id)

    def __iter__(self): 
        return iter([self.top(), self.right(), self.bottom(), self.left()])
    
    def rotate(self): self.grid = np.rot90(self.grid)
    def flip(self): self.grid = np.fliplr(self.grid)

    def all_symmetries(self):
        for _ in range(2):
            for _ in range(4):
                yield self.grid
                self.rotate()
            self.flip()

    def orient(self, border, side):
        for _ in self.all_symmetries():
            self_side = getattr(self, side)()
            if self_side == border: return
    
    def crop(self):
        return self.grid[1:-1, 1:-1]

    def plot(self):
        plt.imshow(self.grid)
        plt.show()
    
class Snowball(Tile):
    def __init__(self, tile): self.grid = [[tile]]
    def __repr__(self): return pformat(self.grid)

    def rotate(self):
        self.grid = np.rot90(self.grid)
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
        self.grid = np.vstack([self.grid, new_bottom])
        self.rotate()

    def merge(self):
        grid = np.vstack([
            np.hstack([x.crop() for x in row]) 
            for row in self.grid
        ])
        return Tile('image', grid)

    def step(self, inners, agg):
        self.prepare(agg)
        new_bottom = []
        for sb_tile in self.bottom():
            common_border = sb_tile.bottom()
            common_key = key(common_border)

            nb_tile = (agg[common_key] - {sb_tile}).pop()
            nb_tile.orient(common_border, 'top')
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
        grid = np.array([
            [(x=='#')*255 for x in row] 
            for row in grid
        ], np.uint8)
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

def monster_dots(dots):
    monster = [
        '                  # ',
        '#    ##    ##    ###',
        ' #  #  #  #  #  #   '
    ]
    for dot in dots:
        m_dots = [ 
            (dot[0] + y-1, dot[1] + x) 
            for y, x, v in iterate(monster) 
            if v == '#' 
        ]
        if all((md in dots) for md in m_dots):
            yield from m_dots

def fst_star(snowball):
    return snowball.top()[0].id * snowball.top()[-1].id * snowball.bottom()[0].id * snowball.bottom()[-1].id

def snd_star(snowball):
    image = snowball.merge()
    m_dots = list(chain.from_iterable(
        monster_dots(to_dots(grid))
        for grid in image.all_symmetries()
    ))
    return len(to_dots(image.grid)) - len(m_dots)
    
if __name__ == '__main__':
    snowball = reassemble(parse(open('data/day20_test.in').read()))
    assert fst_star(snowball) == 20899048083289
    assert snd_star(snowball) == 273

    snowball = reassemble(parse(open('data/day20.in').read()))
    print(fst_star(snowball))
    print(snd_star(snowball))


