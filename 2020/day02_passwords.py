# https://adventofcode.com/2020/day/2

import re

def parse(line):
    PATTERN = r'(\d+)-(\d+) ([a-z]): ([a-z]+)'
    a, b, char, password = re.match(PATTERN, line).groups()
    return int(a), int(b), char, password

def fst_star(line):
    lo, hi, char, password = parse(line)
    return int(lo) <= password.count(char) <= int(hi)

def snd_star(line):
    a, b, char, password = parse(line)
    return (password[a-1] == char) ^ (password[b-1] == char)

if __name__ == '__main__':
    print(sum(map(fst_star, open('data/day02.in'))))
    print(sum(map(snd_star, open('data/day02.in'))))