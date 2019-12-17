# https://adventofcode.com/2019/day/5

from intcode import run

TEST = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]

if __name__ == '__main__':
    code = [*map(int, open('data/day05.in').read().split(','))]
    
    assert next(run([3,0,4,0,99], [1])) == 1

    assert next(run(TEST, [1])) == 999
    assert next(run(TEST, [8])) == 1000
    assert next(run(TEST, [88])) == 1001

    print(*run(code, [1]))
    print(*run(code, [5]))