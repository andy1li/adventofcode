# https://adventofcode.com/2021/day/5

from collections import Counter
import re

def cmp(a, b): return (b > a) - (b < a)

class Line:
    def __init__(self, raw):
        nums = re.findall('\d+', raw)
        self.x1, self.y1, self.x2, self.y2 = map(int, nums)
        self.delta_x = cmp(self.x1, self.x2)
        self.delta_y = cmp(self.y1, self.y2)
        self.diagnal = bool(self.delta_x and self.delta_y)

    def __repr__(self):
        return f'{self.x1},{self.y1} -> {self.x2},{self.y2}'

    def __iter__(self):
        yield from (
            (self.x1 + i * self.delta_x, 
             self.y1 + i * self.delta_y)
            for i in range(1 + max(
                abs(self.x2-self.x1), 
                abs(self.y2-self.y1)
            ))
        )

def count(lines, diagnal=False): 
    cnt = Counter( xy
        for line in lines
        if diagnal or line.diagnal == diagnal
        for xy in line
    )
    return sum( c >= 2 for c in cnt.values() )

TEST = '''\
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2'''.splitlines()

if __name__ == '__main__':
    lines = list(map(Line, TEST))
    assert count(lines) == 5
    assert count(lines, True) == 12 

    lines = list(map(Line, open('data/day05.in')))
    print(count(lines))
    print(count(lines, True))