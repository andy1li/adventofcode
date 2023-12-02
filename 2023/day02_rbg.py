# https://adventofcode.com/2023/day/2

from collections import defaultdict 
from math import prod

def parse_count(raw):
    count, color = raw.split()
    return color, int(count) 

def parse_game(raw):
    _, sets = raw.split(': ')
    counts = sets.replace(';', ',').split(', ')
    return list(map(parse_count, counts))

def parse_games(raw):
    return list(map(parse_game, raw))

def check_game(game):
    MAX = { 'red': 12, 'green': 13, 'blue': 14 }
    return all(count <= MAX[color] for color, count in game)

def fst_star(games):
    return sum( i
        for i, game in enumerate(games, start=1)
        if check_game(game)
    )

def upperbound(game):
    ub = defaultdict(int)
    for color, count in game:
        ub[color] = max(ub[color], count)
    return ub

def snd_star(games):
    upperbounds = map(upperbound, games)
    return sum( prod(ub.values()) for ub in upperbounds )

TEST = '''\
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''.splitlines()

if __name__ == '__main__':
    games = parse_games(TEST)
    assert fst_star(games) == 8
    assert snd_star(games) == 2286
    
    games = parse_games(open('data/day02.in').readlines())
    print(fst_star(games))
    print(snd_star(games))
