# https://adventofcode.com/2022/day/15

import re
from collections import namedtuple

Sensor = namedtuple('Sensor', 'x, y, r')

def parse_sensors(raw):
    def parse_sensor(raw):
        PATTERN = r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)'
        sx, sy, bx, by = list(map(int, re.match(PATTERN, raw).groups()))
        return Sensor(sx, sy, abs(sx-bx)+abs(sy-by))
    return list(map(parse_sensor, raw))

def fst_star(data): 
    pass

def snd_star(data):
    pass

TEST = '''\
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3'''.splitlines()

if __name__ == '__main__':
    sensors = parse_sensors(TEST)
    print(sensors)
    # print(fst_star(data))
    # print(snd_star(data))

    # data = parse_sensors(open('data/day15.in'))
    # print(fst_star(data))
    # print(snd_star(data))