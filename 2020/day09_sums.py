# https://adventofcode.com/2020/day/9

from itertools import accumulate

def find_invalid(data, start=25):
    def is_valid(i):
        A, n = data[i-25:i], data[i]
        needs = {n - x: i for i, x in enumerate(A)}
        return any(
            x in needs and i != needs[x]
            for i, x in enumerate(A)
        )
    return next( data[i] 
        for i in range(start, len(data)) 
        if not is_valid(i)
    )

def find_weakness(data, start=25):
    n = len(data)
    target = find_invalid(data, start)
    acc = list(accumulate(data)) 
    return next(
        min(data[i+1:j]) + max(data[i+1:j])
        for i in range(n)
        for j in range(i+2, n)
        if acc[j] - acc[i] == target
    )

TEST = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]

if __name__ == '__main__':
    assert find_invalid(TEST, start=5) == 127
    assert find_weakness(TEST, start=5) == 62
    data = [*map(int, open('data/day09.in'))]
    print(find_invalid(data))
    print(find_weakness(data))