# https://adventofcode.com/2020/day/24

from collections import Counter
from itertools import product

DELTAS = [
         0+1j, 1+1j, 
    -1+0j,         1+0j,
        -1-1j, 0-1j,
]

def parse(raw):
    def parse_path(line):
        path = iter(line)
        while True:
            try:
                c = next(path)
                if c in 'we': yield c
                else: yield c + next(path) 
            except StopIteration: break
    
    deltas = dict(zip(['nw', 'ne', 'w', 'e', 'sw', 'se'], DELTAS))
    flips = (sum(map(deltas.get, parse_path(line))) for line in raw)
    return { tile for tile, cnt in Counter(flips).items() if cnt&1 }    

def solve(blacks, n=100):
    for _ in range(n):
        neighbors = map(sum, product(blacks, DELTAS))
        blacks = { tile
            for tile, cnt in Counter(neighbors).items()
            if cnt == 2 or (tile in blacks and cnt == 1) 
        }
    return len(blacks)

TEST = '''\
sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew'''.splitlines()

if __name__ == '__main__':
    assert len(parse(TEST)) == 10
    assert solve(parse(TEST)) == 2208
    blacks = parse(open('data/day24.in'))
    print(len(blacks))
    print(solve(blacks))


