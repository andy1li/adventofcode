# https://adventofcode.com/2019/day/9

from intcode import run

TEST1 = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
TEST2 = [1102,34915192,34915192,7,4,7,99,0]
TEST3 = [104,1125899906842624,99]

if __name__ == '__main__':
    assert [*run(TEST1, [])] == TEST1
    assert len(str(next(run(TEST2, [])))) == 16
    assert next(run(TEST3, [])) == 1125899906842624

    code = [*map(int, open('data/day09.in').read().split(','))]
    print(*run(code, [1]))
    print(*run(code, [2]))