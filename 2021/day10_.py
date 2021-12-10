# https://adventofcode.com/2021/day/10

from statistics import median

EXPECTED = { ')': '(', ']': '[', '}': '{', '>': '<' }
CORRUPT = { ')': 3, ']': 57, '}': 1197, '>': 25137 }
COMPLETE = '([{<'

def corrupt(line):
    stack = []
    for x in line:
        if x in '([{<': stack += x,
        elif x in ')]}>':
            if stack[-1] != EXPECTED[x]: return CORRUPT[x]
            stack.pop()
    return 0

def fst_star(lines): 
    return sum(map(corrupt, lines))

def complete(line):
    stack = []
    for x in line:
        if x in '([{<': stack += x,
        elif x in ')]}>':
            stack.pop()
    score = 0
    for x in reversed(stack):
        score *= 5
        score += COMPLETE.index(x) + 1
    return score

def snd_star(lines):
    return median(
        map(complete,
            filter(lambda x: not corrupt(x), lines)
        )
    )

TEST = '''\
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]'''.splitlines()

if __name__ == '__main__':
    assert fst_star(TEST) == 26397
    assert snd_star(TEST) == 288957

    lines = open('data/day10.in').readlines()
    print(fst_star(lines))
    print(snd_star(lines))