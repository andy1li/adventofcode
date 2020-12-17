# https://adventofcode.com/2020/day/16

from z3 import *
from math import prod
import re

def parse_rules(raw):
    def parse_rule(line):
        field, ranges = line.split(': ')
        return field, [*map(int, re.findall(r'\d+', ranges))]
    return dict(map(parse_rule, raw))

def parse_tickets(raw):
    return [ [int(x) for x in line.split(',')] for line in raw ]

def is_valid(ranges, x):
    lo, hi, lo2, hi2 = ranges
    return lo<=x<=hi or lo2<=x<=hi2

def invalid_fields(rules, ticket):
    return [ x
        for x in ticket
        if all(not is_valid(ranges, x) for ranges in rules.values())
    ]

def determine_fields(rules, tickets):
    valids = [t for t in tickets if not invalid_fields(rules, t)]
    s, fields = Solver(), {}

    for f, ranges in rules.items():
        fields[f] = Int(f)
        candiates = ( i
            for i, c in enumerate(zip(*valids)) 
            if all(is_valid(ranges, x) for x in c)
        )
        s.add( Or([ fields[f] == c for c in candiates ]) )

    s.add( Distinct(list(fields.values())) )
    s.check(); m = s.model()

    return { f: m[v].as_long() for f, v in fields.items() }

def fst_star(rules, tickets): 
    return sum( sum(invalid_fields(rules, t)) for t in tickets )

def snd_star(fields, tkt): 
    return prod( tkt[i] for f, i in fields.items() if f.startswith('departure') )

TEST_RULES1 = '''\
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50'''.splitlines()

TEST_TICKETS1 = '''\
7,3,47
40,4,50
55,2,20
38,6,12'''.splitlines()

TEST_RULES2 = '''\
class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19'''.splitlines()

TEST_TICKETS2 = '''\
3,9,18
15,1,5
5,14,9'''.splitlines()

if __name__ == '__main__':
    assert fst_star(parse_rules(TEST_RULES1), parse_tickets(TEST_TICKETS1)) == 71
    # print(determine_fields(parse_rules(TEST_RULES2), parse_tickets(TEST_TICKETS2)))
    rules = parse_rules(open('data/day16_rules.in'))
    tickets = parse_tickets(open('data/day16_tickets.in'))
    print(fst_star(rules, tickets))
    tkt = [73,101,67,97,149,53,89,113,79,131,71,127,137,61,139,103,83,107,109,59]
    print(snd_star(determine_fields(rules, tickets), tkt))
