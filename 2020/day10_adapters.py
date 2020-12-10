# https://adventofcode.com/2020/day/10

from collections import Counter

def get_diffs(data):
    data = [0] + sorted(data) + [max(data)+3]
    return [b-a for a, b in zip(data, data[1:])]

def fst_star(data): 
    cnt = Counter(get_diffs(data))
    return cnt[1] * cnt[3]

def snd_star(data):
    dp = [1] + [0] * max(data)
    for x in sorted(data):
        dp[x] = sum(dp[max(0, x-3) : x])
    return dp[-1]

TEST1 = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
TEST2 = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3 ]

if __name__ == '__main__':
    assert sum(get_diffs(TEST1)) == 22
    assert fst_star(TEST2) == 220
    assert snd_star(TEST1) == 8
    assert snd_star(TEST2) == 19208
    data = [*map(int, open('data/day10.in'))]
    print(fst_star(data))
    print(snd_star(data))