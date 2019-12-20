# https://adventofcode.com/2019/day/20

from advent import get_neighbor_items, iterate, within_bounds
from collections import defaultdict
from matplotlib import pyplot as plt
from string import ascii_uppercase as LETTERS
import networkx

def parse_portal(maze, y, x, val):
    neighbor_items = list(get_neighbor_items(maze, y, x))
    try:
        pos = next( neighbor
            for neighbor, nval in neighbor_items
            if nval == '.'
        )
        name2 = next( (neighbor, nval)
            for neighbor, nval in neighbor_items
            if nval in LETTERS
        )
    except StopIteration:
        name2 = next( (neighbor, nval)
            for neighbor, nval in neighbor_items
            if nval in LETTERS
        )
        pos = next( nneighbor
            for nneighbor, nnval in get_neighbor_items(maze, *name2[0])
            if nnval == '.'
        )
    name1 = (y, x), val
    name = sorted([name1, name2])
    name = name[0][-1] + name[1][-1]
    return name, pos

def parse_graph_portals(maze):
    G, seen = networkx.Graph(), set()
    portals = defaultdict(set)
    for y, x, val in iterate(maze):
        if val == '.':
            for neighbor, nval in get_neighbor_items(maze, y, x):
                if (neighbor not in seen) and nval == '.': 
                    G.add_edge((y, x), neighbor)
            seen.add((y, x))
        if val in LETTERS:
            name, pos = parse_portal(maze, y, x, val)
            if name == 'AA': start = pos
            elif name == 'ZZ': end = pos 
            else: portals[name].add(pos) 
    return G, start, end, portals

def partition_portals(maze, portals):
    inners, outers = {}, {}
    cy, cx = len(maze)//2, len(maze[0])//2
    for name, portal_set in portals.items():
        i, o = sorted(portal_set, 
            key=lambda yx: (yx[0]-cy)**2+(yx[1]-cx)**2
        )
        inners[name] = i
        outers[name] = o
    return inners, outers

def parse(maze, depth=1):
    G, start, end, portals = parse_graph_portals(maze)
    inners, outers = partition_portals(maze, portals)

    H = networkx.Graph()
    for i in range(depth):
        H.add_edges_from([(i, a), (i, b)] for a, b in G.edges)

    if depth == 1: links = [(0, 0)]
    else: links = [*zip(range(depth), range(1, depth))]

    H.add_edges_from(
        [(a, i), (b, outers[n])]
        for a, b in links
        for n, i in inners.items()
    )

    # for d, pos in networkx.shortest_path(H, (0, start), (0, end)):
    #     for n, ipos in inners.items():
    #         if pos == ipos: print(d, n, pos)
    #     for n, opos in outers.items():
    #         if pos == opos: print(d, n, pos)
    return H, (0, start), (0, end)

def shortest_path(G, start, end): 
    # networkx.draw(G, with_labels=True); plt.show()
    return networkx.shortest_path_length(G, start, end)

def recursive(maze): 
    i = 2
    while True:
        try:
            return i, shortest_path(*parse(maze, i))
        except networkx.exception.NetworkXNoPath:
            i += 1

TEST1 = '''         A           
         A           
  #######.#########  
  #######.........#  
  #######.#######.#  
  #######.#######.#  
  #######.#######.#  
  #####  B    ###.#  
BC...##  C    ###.#  
  ##.##       ###.#  
  ##...DE  F  ###.#  
  #####    G  ###.#  
  #########.#####.#  
DE..#######...###.#  
  #.#########.###.#  
FG..#########.....#  
  ###########.#####  
             Z       
             Z       '''.split('\n')
TEST2 = '''                   A               
                   A               
  #################.#############  
  #.#...#...................#.#.#  
  #.#.#.###.###.###.#########.#.#  
  #.#.#.......#...#.....#.#.#...#  
  #.#########.###.#####.#.#.###.#  
  #.............#.#.....#.......#  
  ###.###########.###.#####.#.#.#  
  #.....#        A   C    #.#.#.#  
  #######        S   P    #####.#  
  #.#...#                 #......VT
  #.#.#.#                 #.#####  
  #...#.#               YN....#.#  
  #.###.#                 #####.#  
DI....#.#                 #.....#  
  #####.#                 #.###.#  
ZZ......#               QG....#..AS
  ###.###                 #######  
JO..#.#.#                 #.....#  
  #.#.#.#                 ###.#.#  
  #...#..DI             BU....#..LF
  #####.#                 #.#####  
YN......#               VT..#....QG
  #.###.#                 #.###.#  
  #.#...#                 #.....#  
  ###.###    J L     J    #.#.###  
  #.....#    O F     P    #.#...#  
  #.###.#####.#.#####.#####.###.#  
  #...#.#.#...#.....#.....#.#...#  
  #.#####.###.###.#.#.#########.#  
  #...#.#.....#...#.#.#.#.....#.#  
  #.###.#####.###.###.#.#.#######  
  #.#.........#...#.............#  
  #########.###.###.#############  
           B   J   C               
           U   P   P               '''.split('\n')
TEST3 = '''             Z L X W       C                 
             Z P Q B       K                 
  ###########.#.#.#.#######.###############  
  #...#.......#.#.......#.#.......#.#.#...#  
  ###.#.#.#.#.#.#.#.###.#.#.#######.#.#.###  
  #.#...#.#.#...#.#.#...#...#...#.#.......#  
  #.###.#######.###.###.#.###.###.#.#######  
  #...#.......#.#...#...#.............#...#  
  #.#########.#######.#.#######.#######.###  
  #...#.#    F       R I       Z    #.#.#.#  
  #.###.#    D       E C       H    #.#.#.#  
  #.#...#                           #...#.#  
  #.###.#                           #.###.#  
  #.#....OA                       WB..#.#..ZH
  #.###.#                           #.#.#.#  
CJ......#                           #.....#  
  #######                           #######  
  #.#....CK                         #......IC
  #.###.#                           #.###.#  
  #.....#                           #...#.#  
  ###.###                           #.#.#.#  
XF....#.#                         RF..#.#.#  
  #####.#                           #######  
  #......CJ                       NM..#...#  
  ###.#.#                           #.###.#  
RE....#.#                           #......RF
  ###.###        X   X       L      #.#.#.#  
  #.....#        F   Q       P      #.#.#.#  
  ###.###########.###.#######.#########.###  
  #.....#...#.....#.......#...#.....#.#...#  
  #####.#.###.#######.#######.###.###.#.#.#  
  #.......#.......#.#.#.#.#...#...#...#.#.#  
  #####.###.#####.#.#.#.#.###.###.#.###.###  
  #.......#.....#.#...#...............#...#  
  #############.#.#.###.###################  
               A O F   N                     
               A A D   M                     '''.split('\n')

if __name__ == '__main__':
    assert shortest_path(*parse(TEST1)) == 23
    assert shortest_path(*parse(TEST2)) == 58
    assert shortest_path(*parse(TEST3, 11)) == 396

    maze = open('data/day20.in').readlines()
    print(shortest_path(*parse(maze)))
    print(recursive(maze))