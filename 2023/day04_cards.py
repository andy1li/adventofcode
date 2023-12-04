# https://adventofcode.com/2023/day/4

def parse_numbers(raw):
    return set(map(int, raw.split()))

def parse_card(line):
    _, numbers = line.split(': ')
    wins, haves = numbers.split(' | ')
    return len(parse_numbers(wins) & parse_numbers(haves))

def parse(raw):
    return list(map(parse_card, raw))

def fst_star(cards):
    return sum(2 ** (hits - 1) for hits in cards if hits)

def snd_star(cards):
    count = [1] * len(cards)
    for i, hits in enumerate(cards):
        for j in range(i + 1, min(len(cards), i + hits + 1)):
            count[j] += count[i]
    return sum(count)
    
TEST = '''\
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''.splitlines()

if __name__ == '__main__':
    cards = parse(TEST)
    assert fst_star(cards) == 13
    assert snd_star(cards) == 30
    
    cards = list(parse(open('data/day04.in').readlines()))
    print(fst_star(cards))
    print(snd_star(cards))
