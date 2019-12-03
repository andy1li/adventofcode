# https://adventofcode.com/2018/day/5

from string import ascii_lowercase

def fst_star(polymer):
    stack = []
    for x in polymer:
        if (not stack 
        or abs(ord(x)-ord(stack[-1])) != 0x20): 
            stack.append(x)
        else: 
            stack.pop()
        
    return len(stack)

def try_remove(polymer, type):
    return fst_star(polymer
        .replace(type, '')
        .replace(type.upper(), '')
    )

def snd_star(polymer):
    return min (
        try_remove(polymer, type)
        for type in ascii_lowercase
    )

if __name__ == '__main__':
    TEST = 'dabAcCaCBAcCcaDA'
    assert fst_star(TEST) == 10
    assert snd_star(TEST) == 4

    polymer = open('data/day05.in').read()
    print(fst_star(polymer))
    print(snd_star(polymer))