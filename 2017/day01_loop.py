# https://adventofcode.com/2017/day/1

def sum_match(raw, easy=True):
    loop = list(map(int, raw))
    x = 1 if easy else len(loop)//2
    n = len(loop)
    return sum( loop[i]
        for i in range(n)
        if loop[i] == loop[(i+x) % n]
    )

if __name__ == '__main__':
    assert sum_match('1122') == 3
    assert sum_match('1111') == 4
    assert sum_match('1234') == 0
    assert sum_match('91212129') == 9
    assert sum_match('1212', False) == 6
    assert sum_match('1221', False) == 0
    assert sum_match('123425', False) == 4
    assert sum_match('123123', False) == 12
    assert sum_match('12131415', False) == 4

    raw = open('data/day01.in').read()
    print(sum_match(raw))
    print(sum_match(raw, False))