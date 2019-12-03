# https://adventofcode.com/2018/day/4

from collections import Counter, defaultdict

def parse_record(line): 
    ts, token = line[:17], line[19:]
    minute = int(ts[-2:])
    if 'Guard' in token: token = int(token.split()[1][1:])
    return minute, token

def aggregate(input):
    agg = defaultdict(Counter)
    guard = start = None
    for minute, token in map(parse_record, sorted(input)):
        if type(token) is int: guard = token
        elif 'falls' in token: start = minute
        else: # wakes up
            for i in range(start, minute):
                agg[guard][i] += 1
    return agg

def fst_star(agg):
    guard  = max(agg, key=lambda g: sum(agg[g].values()))
    minute = max(agg[guard], key=lambda m: agg[guard][m])
    return guard * minute

def snd_star(agg):
    (_, minute), guard = max(
        (max((c, m) for m, c in agg[guard].items()), guard)
        for guard in agg
    )
    return guard * minute

TEST = '''[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up'''.split('\n')

if __name__ == '__main__':
    assert fst_star(aggregate(TEST)) == 240
    assert snd_star(aggregate(TEST)) == 4455

    agg = aggregate(open('data/day04.in'))
    print(fst_star(agg))
    print(snd_star(agg))