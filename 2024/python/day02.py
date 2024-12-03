# https://adventofcode.com/2024/day/1


Report = tuple[int, ...]


def parse_report(line) -> Report:
    return tuple(map(int, line.split()))


def parse_reports(lines) -> list[Report]:
    return list(map(parse_report, lines))


def is_safe(report: Report) -> bool:
    Δ = [a - b for a, b in zip(report, report[1:])]
    return all(1 <= d <= 3 for d in Δ) or all(-3 <= d <= -1 for d in Δ)


def is_safe_damper(report: Report) -> bool:
    return is_safe(report) or any(
        is_safe(report[:i] + report[i + 1 :]) for i in range(len(report))
    )


def fst_star(reports) -> int:
    return sum(map(is_safe, reports))


def snd_star(reports) -> int:
    return sum(map(is_safe_damper, reports))


TEST = """\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9""".splitlines()


if __name__ == "__main__":
    reports = parse_reports(TEST)
    assert fst_star(reports) == 2
    assert snd_star(reports) == 4

    lines = open("2024/data/day02.in").readlines()
    reports = parse_reports(lines)
    print(fst_star(reports))
    print(snd_star(reports))
