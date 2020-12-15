# https://adventofcode.com/2020/day/15

from collections import defaultdict, deque

def play(seed, stop=2020): 
    prev, mem = seed[-1], {x: i for i, x in enumerate(seed)}
    for i in range(len(mem), stop):
        if not i % 3e6: print(f'={i/stop:3.0%}')
        mem[prev], prev = i-1, (0 if (prev not in mem) else i-1 - mem[prev])
    return prev

if __name__ == '__main__':
    assert play([0,3,6]) == 436
    assert play([1,3,2]) == 1
    assert play([2,1,3]) == 10
    assert play([1,2,3]) == 27
    assert play([2,3,1]) == 78
    assert play([3,2,1]) == 438
    assert play([3,1,2]) == 1836
    # assert play([0,3,6]), stop=30000000) == 175594
    print(play([1,12,0,20,8,16]))
    # print(play([1,12,0,20,8,16], stop=30000000))