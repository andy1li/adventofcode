# https://adventofcode.com/2020/day/5

def parse(seat):
    binary = seat.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
    return int(binary, 2)

TEST = '''\
BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL'''.splitlines()

if __name__ == '__main__':
    assert list(map(parse, TEST)) == [567, 119, 820]
    seats = set(map(parse, open('data/day05.in')))
    print(max(seats)) # first star
    my_seat = lambda s: s not in seats and {s-1, s+1} <= seats
    print(next(filter(my_seat, range(8, 1024-8)))) # second star