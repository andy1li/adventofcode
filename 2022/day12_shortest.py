# https://adventofcode.com/2022/day/12

from advent import iterate, neighbor_items
from networkx import DiGraph, shortest_path_length, exception

def parse_graph(grid):
    starts = []
    for y, x, val in iterate(grid):
        if val in 'aS': starts += (y, x),
        if val == 'S': start = y, x
        if val == 'E': end = y, x

    for i in range(len(grid)):
        grid[i] = grid[i].replace('S', 'a').replace('E', 'z')

    G = DiGraph([
        ((y, x), (ny, nx))
        for y, x, val in iterate(grid)
        for (ny, nx), nval in neighbor_items(grid, y, x)
        if ord(nval) - ord(val) < 2
    ])
    return G, start, end, starts

fst_star = shortest_path_length

def snd_star(G, starts, end):
    def steps(start):
        try: 
            return shortest_path_length(G, start, end)
        except exception.NetworkXNoPath: 
            return float('inf')
    return min(map(steps, starts))

TEST = '''\
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi'''.splitlines()

if __name__ == '__main__':
    G, start, end, starts = parse_graph(TEST)
    assert fst_star(G, start, end) == 31
    assert snd_star(G, starts, end) == 29

    G, start, end, starts = parse_graph(open('data/day12.in').read().splitlines())
    print(fst_star(G, start, end))
    print(snd_star(G, starts, end))