# https://adventofcode.com/2022/day/6

def solve(stream, n=4): 
    return next( i 
        for i in range(n, len(stream)+1) 
        if len(set(stream[i-n:i])) == n
    )

TEST0 = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
TEST1 = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
TEST2 = 'nppdvjthqldpwncqszvftbrmjlhg'
TEST3 = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
TEST4 = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'

if __name__ == '__main__':
    assert solve(TEST0) == 7
    assert solve(TEST1) == 5
    assert solve(TEST2) == 6
    assert solve(TEST3) == 10
    assert solve(TEST4) == 11
    assert solve(TEST0, 14) == 19
    assert solve(TEST1, 14) == 23
    assert solve(TEST2, 14) == 23
    assert solve(TEST3, 14) == 29
    assert solve(TEST4, 14) == 26

    stream = open('data/day06.in').read().strip()
    print(solve(stream))
    print(solve(stream, n=14))