# https://adventofcode.com/2024/day/3

import re


def fst_star(raw) -> int:
    MUL = re.compile(r"mul\((\d+),(\d+)\)")
    return sum(int(a) * int(b) for a, b in MUL.findall(raw))


def snd_star(raw) -> int:
    total, enabled = 0, True
    for part in re.split(r"(do\(\)|don't\(\))", raw):
        match part:
            case "do()":
                enabled = True
            case "don't()":
                enabled = False
            case _:
                total += enabled and fst_star(part)
    return total


TEST1 = "mul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
TEST2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

if __name__ == "__main__":
    assert fst_star(TEST1) == 161
    assert snd_star(TEST2) == 48

    raw = open("2024/data/day03.in").read()
    print(fst_star(raw))
    print(snd_star(raw))
