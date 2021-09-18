# https://adventofcode.com/2017/day/3

def get_pos(x):
    return 0, 0

if __name__ == '__main__':
    assert checksum(parse(TEST1)) == 18
    assert checksum(parse(TEST2), divisible) == 9

