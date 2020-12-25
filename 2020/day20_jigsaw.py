# https://adventofcode.com/2020/day/20

from advent import iterate
from collections import defaultdict
from itertools import chain
from matplotlib import pyplot as plt
import numpy as np
import math

class Tile:
    def __init__(self, id, grid):
        self.id = id 
        self.grid = grid

    __repr__ = lambda self: self.id
    rotate = lambda self: Tile(self.id, np.rot90(self.grid))
    flip = lambda self: Tile(self.id, np.fliplr(self.grid))
    crop = lambda self: self.grid[1:-1, 1:-1]
    dots = lambda self: { (y, x) for y, x, v in iterate(self.grid) if v }
    
    @property
    def edges(self): # 0-3: top right bottom left
        return [*map(tuple, (
            self.grid[0], self.grid[...,-1], self.grid[-1], self.grid[...,0]
        ))]

    def symmetries(self):
        for _ in range(4):
            yield self; yield self.flip()
            self = self.rotate()

    def match(self, agg, side):
        edge = self.edges[side]
        other = next(t for t in agg[key(edge)] if t.id != self.id)
        return next( o
            for o in other.symmetries()
            if o.edges[(side+2)%4] == edge
        )

    def plot(self):
        plt.imshow(self.grid, cmap='viridis')
        plt.grid(False)
        plt.show()

def parse(raw):
    def parse_tile(raw):
        id, *grid = raw.splitlines()
        grid = list(map(tuple, grid))
        return Tile(id[5:-1], np.array(grid) == '#')
    return {parse_tile(r) for r in raw.split('\n\n')}

key = lambda edge: min([edge, edge[::-1]])

def aggregate(tiles):  
    agg = defaultdict(list)
    for tile in tiles:
        for edge in tile.edges:
            agg[key(edge)] += tile,
    return agg

def merge(tiles):
    grid = np.vstack([np.hstack([x.crop() for x in row]) for row in tiles])
    return Tile('image', grid)

def assemble(tiles, n=12):
    n_tiles = lambda edge: len(agg[key(edge)])
    is_corner = lambda t: sum(n_tiles(e)==1 for e in t.edges) == 2

    def extend(tile, side):
        xs = [tile]
        for _ in range(n-1):
            xs += xs[-1].match(agg, side),
        return xs

    agg = aggregate(tiles)
    corners = list(filter(is_corner, tiles))
    start = next( c for c in corners 
        if 2 == n_tiles(c.edges[1]) == n_tiles(c.edges[2])
    )
    tiles = [ extend(x, side=1) for x in extend(start, side=2) ]
    return corners, merge(tiles)

def monster_dots(image):
    monster = ['                  # ',
               '#    ##    ##    ###',
               ' #  #  #  #  #  #   ']
    dots = image.dots()
    for y, x in dots:
        m_dots = [ (y + dy-1, x + dx) 
            for dy, dx, v in iterate(monster) if v == '#' 
        ]
        if all((md in dots) for md in m_dots):
            yield from m_dots

def fst_star(corners):
    return math.prod(int(c.id) for c in corners)

def snd_star(image):
    m_dots = list(chain(*map(monster_dots, image.symmetries())))
    return len(image.dots()) - len(m_dots)
    
if __name__ == '__main__':
    tiles = parse(open('data/day20_test.in').read())
    corners, image = assemble(tiles, n=3)
    assert fst_star(corners) == 20899048083289
    assert snd_star(image) == 273
    
    tiles = parse(open('data/day20.in').read())
    corners, image = assemble(tiles)
    print(fst_star(corners))
    print(snd_star(image))
    # image.plot()