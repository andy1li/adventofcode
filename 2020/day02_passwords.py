# https://adventofcode.com/2020/day/2

from collections import Counter
import re

def parse(line):
    PATTERN = r'(\d+)-(\d+) ([a-z]): ([a-z]+)'
    a, b, letter, password = re.match(PATTERN, line).groups()
    return int(a), int(b), letter, password

def fst_star(line):
    lo, hi, letter, password = parse(line)
    return int(lo) <= Counter(password)[letter] <= int(hi)

def snd_star(line):
    a, b, letter, password = parse(line)
    return (password[a-1] == letter) != (password[b-1] == letter)

if __name__ == '__main__':
    print(sum(map(fst_star, open('data/day02.in'))))
    print(sum(map(snd_star, open('data/day02.in'))))