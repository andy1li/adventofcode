# https://adventofcode.com/2018/day/13

from typing import NamedTuple

class Cart(NamedTuple):
    y: int; x: int; 
    dir: int; turn: int = 0

    def step(self, tracks):
        y, x, dir, turn = self
        y += [-1, 0, 1, 0][dir]
        x += [ 0, 1, 0,-1][dir]

        track = tracks[y][x]
        if track == '+':
            dir = (dir + turn-1) % 4
            turn = (turn+1) % 3
        elif track == '/' : dir = int('1032'[dir])
        elif track == '\\': dir = int('3210'[dir])
        else: assert track in '-|'

        return Cart(y, x, dir, turn)

def parse(input):
    tracks, carts = [line.strip('\n') for line in input], []
    for y, row in enumerate(tracks):
        for x, piece in enumerate(row):
            if piece in '^>v<':
                carts.append(Cart(y, x, '^>v<'.index(piece)))
                tracks[y] = tracks[y].replace(
                    piece, '|' if piece in '^v' else '-', 1
                )
    return tracks, carts

def show(tracks, carts):
    tracks = tracks.copy()
    for y, x, dir, _ in carts:
        tracks[y] = tracks[y][:x] + '^>v<'[dir] + tracks[y][x+1:]
    print(*tracks, sep='\n', end='\n\n')

def fst_star(tracks, carts):
    while True:
        # show(tracks, carts)
        positions = {(c.y, c.x) for c in carts} 
        for i, c in enumerate(carts):
            positions.discard((c.y, c.x))
            cart = y, x, *_ = c.step(tracks)
            if (y, x) in positions: return x, y
            carts[i] = cart
            positions.add((y, x))
        carts.sort()
        
def snd_star(tracks, carts):
    while True:
        # show(tracks, carts)
        if len(carts) == 1: return carts[0].x, carts[0].y

        new_carts, crashed = [], set()
        positions = {(c.y, c.x) for c in carts}
        for c in carts:
            if (c.y, c.x) in crashed: continue
            positions.discard((c.y, c.x))

            cart = y, x, *_ = c.step(tracks)
            if (y, x) in positions: 
                crashed.add((y, x))
                new_carts = [ c 
                    for c in new_carts
                    if (c[0], c[1]) != (y, x)
                ]
                positions.discard((y, x))
            else:
                new_carts.append(cart)
                positions.add((y, x))

        carts = sorted(new_carts)
        
TEST1 = r'''/->-\        
|   |  /----\
| /-+--+-\  |
| | |  | v  |
\-+-/  \-+--/
  \------/   '''.split('\n')

TEST2 = r'''/>-<\  
|   |  
| /<+-\
| | | v
\>+</ |
  |   ^
  \<->/'''.split('\n')

if __name__ == '__main__':
    assert fst_star(*parse(TEST1)) == (7, 3)
    assert snd_star(*parse(TEST2)) == (6, 4)

    print(fst_star(*parse(open('data/day13.in'))))
    print(snd_star(*parse(open('data/day13.in'))))