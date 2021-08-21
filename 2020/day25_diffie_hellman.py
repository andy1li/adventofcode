# https://adventofcode.com/2020/day/25

from itertools import count
MOD = 20201227

def step(val, subject=7):
    return (subject * val) % MOD

def loop_size(public, val=1, subject=7):
    for i in count(1):
        val = step(val, subject)
        if val == public: return i

def solve(card, door):
    val, subject = 1, card
    for _ in range(loop_size(door)): 
        val = step(val, subject)
    return val

if __name__ == '__main__':
    assert loop_size(5764801) == 8
    assert loop_size(17807724) == 11
    assert solve(5764801, 17807724) == 14897079

    print(solve(1327981, 2822615))

