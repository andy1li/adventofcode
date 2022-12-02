# https://adventofcode.com/2022/day/2

from typing import List, Tuple 

Round = Tuple[str, str]

def parse_rounds(raw) -> List[Round]:
    return [line.split() for line in raw.splitlines()]


opponent, mine = 'ABC', 'XYZ'

def decode(strategy, x):
    return strategy.index(x)

def shape(i): return i + 1

def outcome(a, b): 
    return ((b - a) + 1) % 3 * 3

def fst_star(rounds: List[Round]): 
    def score(round: Round) -> int:        
        a, b = round
        a, b = decode(opponent, a), decode(mine, b)
        return shape(b) + outcome(a, b)

    return sum(map(score, rounds))


def decode_outcome(x):
    return decode(mine, x) 

def reverse_choose(a, outcome):
    a = decode(opponent, a)
    return ((a + outcome - 1) % 3) + 1

def snd_star(rounds: List[Round]):
    def score(round: Round) -> int:
        a, b = round
        outcome = decode_outcome(b)
        return reverse_choose(a, outcome) + outcome * 3

    return sum(map(score, rounds))


TEST = '''A Y
B X
C Z'''

if __name__ == '__main__':
    rounds = parse_rounds(TEST)
    assert fst_star(rounds) == 15
    assert snd_star(rounds) == 12

    rounds = parse_rounds(open('data/day02.in').read())
    print(fst_star(rounds))
    print(snd_star(rounds))