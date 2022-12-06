# https://adventofcode.com/2017/day/10

from functools import reduce
from operator import xor

def parse_lengths(raw):
    return list(map(int, raw.split(',')))
     
def round(circle, skip, offset, lengths, n=256):
    for l in lengths:
        circle = circle[l:] + list(reversed(circle[:l]))
        circle = circle[skip:] + circle[:skip]
        offset += l + skip
        skip = (skip + 1) % n
    return circle, skip, offset
    
def restore(circle, offset):
    return circle[-offset:] + circle[:-offset]

def dense(chunk):
    return hex(reduce(xor, chunk))[2:].zfill(2)

def fst_star(raw, n=256):
    lengths = parse_lengths(raw)
    circle, _, offset = round(list(range(n)), 0, 0, lengths, n)
    circle = restore(circle, offset % n)
    return circle[0] * circle[1]

def snd_star(raw):
    lengths = list(map(ord, raw)) + [17, 31, 73, 47, 23]
    circle, skip, offset = list(range(256)), 0, 0
    for _ in range(64):
        circle, skip, offset = round(circle, skip, offset, lengths)
    circle = restore(circle, offset % 256)

    chunks = (circle[i:i+16] for i in range(0, 256, 16))
    return ''.join(map(dense, chunks))
    
TEST0 = '3,4,1,5'
TEST1 = ''
TEST2 = 'AoC 2017'
TEST3 = '1,2,3'
TEST4 = '1,2,4'

if __name__ == '__main__':
    assert fst_star(TEST0, n=5) == 12
    assert snd_star(TEST1) == 'a2582a3a0e66e6e86e3812dcb672a272'
    assert snd_star(TEST2) == '33efeb34ea91902bb2f59c9920caa6cd'
    assert snd_star(TEST3) == '3efbe78a8d82f29979031a4aa0b16a9d'
    assert snd_star(TEST4) == '63960835bcdc130f0b66d7ff4f6a5a8e'

    raw = open('data/day10.in').read()
    print(fst_star(raw))
    print(snd_star(raw))