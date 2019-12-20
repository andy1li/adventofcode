# https://adventofcode.com/2019/day/18

from advent import get_neighbors, iterate
from functools import lru_cache 
from string import (
    ascii_lowercase as KEYS, 
    ascii_letters as KEYS_OR_DOORS
)

def parse(input):
    maze = [*map(str.strip, input)]
    starts, distances, preqs = tuple(), {}, {} 
    for y, x, val in iterate(maze):
        if val == '@': 
            starts += (y, x),
            d, p = bfs(maze, (y, x))
            distances[y, x] = d
            preqs.update(p)
        if val in KEYS:
            distances[val] = bfs(maze, (y, x))[0]
    return maze, starts, distances, preqs

def bfs(maze, start):
    distance, preq = {}, {}
    q, seen = [(0, start, frozenset())], {start}
    for d, (y, x), p in q:
        val = maze[y][x]
        if val in KEYS:
            distance[val] = d
            preq[val] = p
        if val in KEYS_OR_DOORS: 
            p |= {val.lower()}

        for neighbor in get_neighbors(y, x):
            ny, nx = neighbor
            if (neighbor not in seen and maze[ny][nx] != '#'):
                seen.add(neighbor)
                q.append((d+1, neighbor, p))

    return distance, preq

def shortest_path(maze, starts, distances, preqs):
    @lru_cache(None)
    def recurse(robots, path):
        if len(path) == len(keys): return 0
        return min(
            distances[robot][key] + recurse(
                robots[:i]+(key,)+robots[i+1:], path|{key}
            )
            for key in keys
            for i, robot in enumerate(robots)
            if (key not in path
            and not (preqs[key] - path)
            and key in distances[robot])
        )

    keys = preqs.keys()
    return recurse(starts, frozenset())

TEST1 = '''#########
#b.A.@.a#
#########'''.split()
TEST2 = '''########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################'''.split()
TEST3 = '''########################
#...............b.C.D.f#
#.######################
#.....@.a.B.c.d.A.e.F.g#
########################'''.split()
TEST4 = '''#################
#i.G..c...e..H.p#
########.########
#j.A..b...f..D.o#
########@########
#k.E..a...g..B.n#
########.########
#l.F..d...h..C.m#
#################'''.split()
TEST5 = '''########################
#@..............ac.GI.b#
###d#e#f################
###A#B#C################
###g#h#i################
########################'''.split()

TEST6 = '''#######
#a.#Cd#
##@#@##
#######
##@#@##
#cB#Ab#
#######'''.split()
TEST7 = '''###############
#d.ABC.#.....a#
######@#@######
###############
######@#@######
#b.....#.....c#
###############'''.split()
TEST8 = '''#############
#DcBa.#.GhKl#
#.###@#@#I###
#e#d#####j#k#
###C#@#@###J#
#fEbA.#.FgHi#
#############'''.split()
TEST9 = '''#############
#g#f.D#..h#l#
#F###e#E###.#
#dCba@#@BcIJ#
#############
#nK.L@#@G...#
#M###N#H###.#
#o#m..#i#jk.#
#############'''.split()

if __name__ == '__main__':
    assert shortest_path(*parse(TEST1)) == 8
    assert shortest_path(*parse(TEST2)) == 86
    assert shortest_path(*parse(TEST3)) == 132
    assert shortest_path(*parse(TEST4)) == 136
    assert shortest_path(*parse(TEST5)) == 81

    assert shortest_path(*parse(TEST6)) == 8
    assert shortest_path(*parse(TEST7)) == 24
    assert shortest_path(*parse(TEST8)) == 32
    assert shortest_path(*parse(TEST9)) == 72

    print(shortest_path(*parse(open('data/day18a.in'))))
    print(shortest_path(*parse(open('data/day18b.in'))))