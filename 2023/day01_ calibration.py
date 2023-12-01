# https://adventofcode.com/2023/day/1

NUMBERS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def parse(line):
    digits = [*filter(str.isdigit, line)]
    return int(digits[0] + digits[-1])

def replace(line):
    for i, n in enumerate(NUMBERS, start=1):
        line = line.replace(n, n[0] + str(i) + n[-1])
        # eg. one -> o1e, two -> t2o, ...
    return line

def fst_star(lines):
    return sum(map(parse, lines))

def snd_star(lines):
    return fst_star(map(replace, lines))

TEST1 = '''\
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet'''.splitlines()

TEST2 = '''\
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen'''.splitlines()

if __name__ == '__main__':
    assert fst_star(TEST1) == 142
    assert snd_star(TEST2) == 281
    
    lines = open('data/day01.in').readlines()
    print(fst_star(lines))
    print(snd_star(lines))