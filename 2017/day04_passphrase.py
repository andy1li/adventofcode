# https://adventofcode.com/2017/day/4

from collections import Counter

def parse(raw):
    return [line.split() for line in raw]

def simple_valid(phrase):
    cnt = Counter(phrase)
    return all(v==1 for v in cnt.values())

def anagram_valid(phrase):
    cnt = Counter(''.join(sorted(word)) for word in phrase)
    return all(v==1 for v in cnt.values())

def count_valid(phrases, func=simple_valid):
    return sum(map(func, phrases))

if __name__ == '__main__':
    phrases = parse(open('data/day04.in'))
    print(count_valid(phrases))
    print(count_valid(phrases, anagram_valid))