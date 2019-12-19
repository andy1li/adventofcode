# https://adventofcode.com/2019/day/18

from advent import get_neighbors, iterate
from functools import lru_cache 
from string import ascii_lowercase as KEYS, ascii_uppercase as DOORS

def parse(input):
    maze, keys = [*map(str.strip, input)], {}
    for y, x, val in iterate(maze):
        if val == '@': start = y, x
        if val in KEYS: keys[val] = y, x
    return maze, keys, start

def bfs(maze, start):
    q, distance, seen = [(0, start)], {}, {start}
    for d, (y, x) in q:
        val = maze[y][x]
        if val in KEYS: distance[val] = d
        for neighbor in get_neighbors(y, x):
            val = maze[neighbor[0]][neighbor[1]]
            if (neighbor in seen or val == '#'): continue
            seen.add(neighbor)
            q.append((d+1, neighbor))
    return distance

def get_dep(maze, start):
    dep, seen = {}, {start}
    def dfs(unlocked, pos):
        val = maze[pos[0]][pos[1]]
        if val in KEYS: dep[val] = unlocked
        if val in DOORS: unlocked |= {val.lower()}
        for neighbor in get_neighbors(*pos):
            if (maze[neighbor[0]][neighbor[1]] != '#'
            and neighbor not in seen):
                seen.add(neighbor)
                dfs(unlocked, neighbor)
    dfs(frozenset(), start)
    return dep

# def shortest_path(maze, keys, start): 
#     @lru_cache(None)
#     def recurse(collected, start):
#         if len(collected) == len(keys): return 0
#         return min(
#             distances[start][end] + recurse(collected|{end}, end)
#             for end in keys
#             if (end not in collected
#             and not (dep[end] - collected))
#         )
#     # print(*maze, sep='\n')
#     distances = { key: bfs(maze, pos) 
#         for key, pos in keys.items()
#     }
#     distances[start] = bfs(maze, start)

#     dep = get_dep(maze, start)
#     return recurse(frozenset(), start)

def shortest_path(maze, keys, start): 
    @lru_cache(None)
    def recurse(collected, start):
        if len(collected) == len(keys): return 0
        return min(
            distances[start][end] + recurse(collected|{end}, end)
            for end in keys
            if (end not in collected
            and not (dep[end] - collected))
        )
    # print(*maze, sep='\n')
    distances = { key: bfs(maze, pos) 
        for key, pos in keys.items()
    }
    distances[start] = bfs(maze, start)

    dep = get_dep(maze, start)
    return recurse(frozenset(), start)

def snd_star(data): 
    pass

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

    # print(shortest_path(*parse(open('data/day18a.in'))))
    # print(snd_star(data))