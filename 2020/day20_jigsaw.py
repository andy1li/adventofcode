# https://adventofcode.com/2020/day/20

from collections import defaultdict
from itertools import chain, count, combinations

flatten_ids = lambda tile: tuple(chain(*tile.ids))
count_ids = lambda tile: len(flatten_ids(tile))

class Tile:
    def __init__(self, borders, ids):
        self.borders = borders
        self.ids = ids

    def __iter__(self): return iter(self.borders)
    def __repr__(self): return f'{self.ids}: {self.borders}'
    def __hash__(self): return hash(flatten_ids(self))
    def __eq__(self, other): return flatten_ids(self) == flatten_ids(other)

    def rotate(self):
        return Tile(
            borders = [self.borders[-1]] + self.borders[:-1],
            ids = [row[::-1] for row in zip(*self.ids)]
        )

    def flip(self):
        bs = [b[::-1] for b in self.borders]
        bs[1], bs[3] = bs[3], bs[1]
        return Tile(bs, [row[::-1] for row in self.ids])

    def transform(self, border, row_pos):
        tile = self
        for _ in range(2):
            for _ in range(4):
                if tile.borders[row_pos] == border: return tile
                tile = tile.rotate()
            tile = tile.flip()

    def merge(self, other, border):
        if set(flatten_ids(self)) & set(flatten_ids(other)): 
            return Tile(list('....'), [[0]])

        s = self.transform(border[::-1], 2)
        o = other.transform(border, 0)
        return Tile([
            s.borders[0], s.borders[1] + o.borders[1],
            o.borders[2], o.borders[3] + s.borders[3]
        ], s.ids+o.ids)

def parse(raw):
    def parse_tile(tile):
        tile = tile.splitlines()
        id = int(tile.pop(0)[5:-1])
        return Tile([ 
            tile[0], ''.join(row[-1] for row in tile), 
            tile[-1][::-1], ''.join(row[0] for row in tile)[::-1]
        ], [(id,)])
    return {parse_tile(t) for t in raw.split('\n\n')}
    
seen = set()
def step(tiles):
    matches = defaultdict(list)
    for tile in tiles:
        for border in tile.borders:
            b = tuple(sorted([border, border[::-1]]))
            matches[b].append(tile)

    for border, match in matches.items():
        for t1, t2 in combinations(match, 2):
            pair = (flatten_ids(t1), flatten_ids(t2))
            if pair in seen: continue
            seen.add(pair)
            tiles.add( t1.merge(t2, border[0]) )
            
    return tiles

def reassemble(tiles, slow=False):
    seen.clear()
    n = len(tiles)
    for i in count():
        tiles = step(tiles)
        largest = max(tiles, key=count_ids)
        if slow: print(i, len(tiles), count_ids(largest))

        if count_ids(largest) == n:
            ids = largest.ids
            if slow: print(ids)
            return ids[0][0] * ids[0][-1] * ids[-1][0] * ids[-1][-1]

if __name__ == '__main__':
    test = open('data/day20_test.in').read()
    assert  reassemble(parse(test)) == 20899048083289
    
    tiles = parse(open('data/day20.in').read())
    print(reassemble(tiles, slow=True))
    assembled = [
     (3169, 3761, 2137, 1229, 1039, 1801, 1373, 2411, 3413, 2129, 2029, 1249), 
     (2081, 1321, 2287, 2269, 2251, 3079, 3391, 2971, 1091, 2293, 1697, 1607), 
     (3301, 1571, 3917, 1753, 3583, 2221, 2887, 3797, 1873, 1031, 3923, 2963), 
     (1301, 2417, 2797, 3313, 2393, 3001, 1489, 2143, 3739, 3697, 2477, 2707), 
     (2689, 3541, 1949, 1787, 3907, 3929, 1931, 3659, 1163, 1723, 3733, 1789), 
     (1499, 3049, 3671, 2699, 3163, 2333, 1721, 2423, 2027, 1013, 3767, 1613), 
     (1777, 1297, 3299, 1747, 3643, 2179, 1879, 1429, 2339, 1867, 3209, 3461), 
     (3833, 2063, 1223, 2381, 1069, 3863, 2579, 3257, 1933, 3989, 2237, 1151), 
     (2459, 2593, 2879, 1279, 1997, 1823, 3469, 1553, 3847, 3793, 2273, 1511), 
     (1583, 2383, 3853, 3319, 3931, 1783, 3547, 2791, 3253, 2311, 2549, 1171), 
     (1283, 3727, 1213, 3457, 1523, 1033, 3251, 3167, 2837, 3331, 2731, 1951), 
     (1019, 1399, 2711, 2161, 1871, 1453, 1549, 1097, 1129, 3511, 2719, 3467)]


