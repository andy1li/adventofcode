# https://adventofcode.com/2020/day/19

from collections import defaultdict
import regex

def parse(raw, add_loops=False):
    G = defaultdict(list)
    for line in raw:
        n, sub_rules = line.split(': ')
        for sr in sub_rules.split(' | '):
            if sr[0] == '"': G[n] = sr[1]
            else: G[n].append(sr.split())

    def dfs(n='0'):
        node = G[n]
        if type(node) == str: return node
        if type(node) == list:
            if add_loops and n == '8':
                return '(?P<eight>{0}|{0}(?&eight))'.format(dfs("42"))
            if add_loops and n == '11':
                return '(?P<eleven>{0}{1}|{0}(?&eleven){1})'.format(dfs("42"), dfs("31"))
            else:
                branches = ( ''.join(dfs(x) for x in branch) for branch in node )
                return '(' + '|'.join(branches) + ')'

    return '^' + dfs() + '$'

def count_matches(rule, messeages): 
    return sum(bool(regex.match(rule, m)) for m in messeages) 

TEST_RULES1 = '''\
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"'''.splitlines()

TEST_MESSAGES1 = '''
ababbb
bababa
abbbab
aaabbb
aaaabbb'''.splitlines()

TEST_RULES2 = '''\
42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1'''.splitlines()

TEST_MESSAGES2 = '''
abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba'''.splitlines()

if __name__ == '__main__':
    assert count_matches(parse(TEST_RULES1), TEST_MESSAGES1) == 2
    assert count_matches(parse(TEST_RULES2, add_loops=True), TEST_MESSAGES2) == 12
    rules = open('data/day19_rules.in').readlines()
    messeages = open('data/day19_messages.in').readlines()
    print(count_matches(parse(rules), messeages))
    print(count_matches(parse(rules, add_loops=True), messeages))

