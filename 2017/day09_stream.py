# https://adventofcode.com/2017/day/9

def solve(stream):
    score = depth = removed = 0
    ignore = garbage = False
    for x in stream:
        if ignore    : ignore = False
        elif x == '!': ignore = True
        elif x == '>': garbage = False
        elif garbage : removed += 1
        elif x == '<': garbage = True
        elif x == '{': depth += 1
        elif x == '}': score += depth; depth -= 1
    return score, removed

TEST0 = [
    '{}',
    '{{{}}}',
    '{{},{}}',
    '{{{},{},{{}}}}',
    '{<a>,<a>,<a>,<a>}',
    '{{<ab>},{<ab>},{<ab>},{<ab>}}',
    '{{<!!>},{<!!>},{<!!>},{<!!>}}',
    '{{<a!>},{<a!>},{<a!>},{<ab>}}'
]
TEST1 = [
    '<>',
    '<random characters>',
    '<<<<>',
    '<{!>}>',
    '<!!>',
    '<!!!>>',
    '<{o"i!a,<{i<a>'
]

if __name__ == '__main__':
    assert [solve(case)[0] for case in TEST0] == [1, 6, 5, 16, 1, 9, 9 ,3]
    assert [solve(case)[1] for case in TEST1] == [0, 17, 3, 2, 0, 0, 10]
  
    stream = open('data/day09.in').read()
    print(solve(stream))