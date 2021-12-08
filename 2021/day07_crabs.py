# https://adventofcode.com/2021/day/7

from statistics import median

def parse(raw):
    return sorted(map(int, raw.split(',')))

def fst_star(crabs):
    m = median(crabs)
    return int(sum(abs(x - m) for x in crabs))

def gauss(n):
    return n * (n+1) // 2

def snd_star(crabs):
    return min(
        sum(gauss(abs(x-i)) for x in crabs)
        for i in range(crabs[0], crabs[-1])
    )

TEST = '16,1,2,0,4,2,7,1,2,14'

if __name__ == '__main__':
    assert fst_star(parse(TEST)) == 37
    assert snd_star(parse(TEST)) == 168

    crabs = parse(open('data/day07.in').read())
    print(fst_star(crabs))
    print(snd_star(crabs))