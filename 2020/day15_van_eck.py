# https://adventofcode.com/2020/day/15

def play(seed, stop=2020): 
    n, mem = seed[-1], {x: i for i, x in enumerate(seed)}
    for i in range(len(seed)-1, stop-1):
        # if not i % 3e6: print(f'={i/stop:3.0%}')
        mem[n], n = i, i - mem.get(n, i)
    return n

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
    print(play([1,12,0,20,8,16], stop=30000000))