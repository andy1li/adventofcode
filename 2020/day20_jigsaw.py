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
            self.grid[0], self.grid[...,-1],
            self.grid[-1], self.grid[...,0]
        ))]

    def all_symmetries(self):
        for _ in range(2):
            for _ in range(4):
                yield self
                self = self.rotate()
            self = self.flip()

    def match(self, agg, side):
        edge = self.edges[side]
        other = next(t for t in agg[key(edge)] if t.id != self.id)
        return next( o
            for o in other.all_symmetries()
            if edge == o.edges[(side+2)%4]
        )

    def plot(self):
        plt.imshow(self.grid)
        plt.show()

def parse(raw):
    def parse_tile(raw):
        grid = raw.splitlines()
        id = grid.pop(0)[5:-1]
        grid = list(map(tuple, grid))
        return Tile(id, np.array(grid) == '#')
    return {parse_tile(r) for r in raw.split('\n\n')}

key = lambda b: min([b, b[::-1]])
n_tiles = lambda agg, e: len(agg[key(e)])

def aggregate(tiles):  
    agg = defaultdict(list)
    for tile in tiles:
        for edge in tile.edges:
            agg[key(edge)] += tile,
    return agg

def is_corner(agg, tile):
    return sum(n_tiles(agg, e)==1 for e in tile.edges) == 2

def assemble(tiles, n=12):
    def extend(tile, side):
        xs = [tile]
        for _ in range(n-1):
            xs += xs[-1].match(agg, side),
        return xs

    agg = aggregate(tiles)
    corners = {t for t in tiles if is_corner(agg, t)}
    start = next( c for c in corners 
        if n_tiles(agg, c.edges[1]) == n_tiles(agg, c.edges[2]) == 2
    )
    tiles = [ extend(x, side=1) for x in extend(start, side=2) ]
    return corners, tiles

def merge(tiles):
    grid = np.vstack([
        np.hstack([x.crop() for x in row]) 
        for row in tiles
    ])
    return Tile('image', grid)

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

def fst_star(corners):
    return math.prod(int(c.id) for c in corners)

def snd_star(tiles):
    image = merge(tiles)
    m_dots = list(chain.from_iterable(
        monster_dots(image.dots())
        for image in image.all_symmetries()
    ))
    return len(image.dots()) - len(m_dots)
    
if __name__ == '__main__':
    tiles = parse(open('data/day20_test.in').read())
    corners, tiles = assemble(tiles, n=3)
    assert fst_star(corners) == 20899048083289
    assert snd_star(tiles) == 273
    
    tiles = parse(open('data/day20.in').read())
    corners, tiles = assemble(tiles)
    print(fst_star(corners))
    print(snd_star(tiles))

