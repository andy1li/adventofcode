# https://adventofcode.com/2021/day/6

def parse(raw):
    days = [0] * 9
    for x in map(int, raw.split(',')):
        days[x] += 1
    return days

def step(days):
    days.append( days.pop(0) )
    days[6] += days[-1]
    return days

def exp(days, n=80):
    days = days[:]
    for _ in range(n):
        days = step(days)
    return sum(days)

TEST = '3,4,3,1,2'

if __name__ == '__main__':
    assert exp(parse(TEST)) == 5934
    assert exp(parse(TEST), 256) == 26984457539

    days = parse(open('data/day06.in').read())
    print(exp(days), exp(days, 256))