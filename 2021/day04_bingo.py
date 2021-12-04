# https://adventofcode.com/2021/day/4

import numpy as np

class Board:
    def __init__(self, raw):
        self.grid = np.array([
            [int(x) for x in row.split()] 
            for row in raw.splitlines()
        ])
        self.lines = list(self.grid) + list(self.grid.T)

    def __repr__(self):
        return str(self.grid)

    def has_won(self, sofar):
        return any(
            all(np.isin(line, sofar))
            for line in self.lines    
        )

    def sum_unmarked(self, sofar):
        mask = ~np.isin(self.grid, sofar)
        return self.grid[mask].sum()

def parse_boards(raw):
    return list(map(Board, raw.split('\n\n')))

def play(drawn, boards): 
    scores = {}
    for i, x in enumerate(drawn):
        sofar = drawn[:i+1]
        for b in boards:
            if b.has_won(sofar) and (b not in scores):
               scores[b] = x * b.sum_unmarked(sofar)
    return list(scores.values())    

TEST = '''\
22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7'''

if __name__ == '__main__':
    drawn = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
    scores = play(drawn, parse_boards(TEST))
    assert scores[0] == 4512
    assert scores[-1] == 1924

    drawn = [68,30,65,69,5,78,41,73,55,0,76,98,79,42,37,21,9,34,56,33,64,54,24,43,15,58,61,38,12,20,4,26,87,95,94,89,83,74,97,77,67,40,63,88,19,31,81,80,60,14,18,47,93,57,17,90,84,85,48,6,91,7,86,13,51,53,8,16,23,66,36,39,32,82,72,11,52,28,62,70,59,50,1,46,96,71,35,10,25,22,27,99,29,45,44,3,75,92,49,2]
    boards = parse_boards(open('data/day04.in').read())
    scores = play(drawn, boards)
    print(scores[0], scores[-1])