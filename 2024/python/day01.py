# https://adventofcode.com/2024/day/1


def parse_ints(line):
    return tuple(map(int, line.split()))


def parse_list(lines) -> tuple[list[int], list[int]]:
    return zip(*map(parse_ints, lines))


def fst_star(left: list[int], right: list[int]) -> int:
    return sum(abs(l - r) for l, r in zip(sorted(left), sorted(right)))


def snd_star(left: list[int], right: list[int]) -> int:
    return sum(l * right.count(l) for l in left)


TEST = """\
3   4
4   3
2   5
1   3
3   9
3   3""".splitlines()


if __name__ == "__main__":
    left, right = parse_list(TEST)
    assert fst_star(left, right) == 11
    assert snd_star(left, right) == 31

    left, right = parse_list(open("2024/data/day01.in"))
    print(fst_star(left, right))
    print(snd_star(left, right))
