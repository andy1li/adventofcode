# https://adventofcode.com/2020/day/19

import regex

def parse(raw, add_loops=False):
    G = dict(line.split(': ') for line in raw.splitlines())

    def dfs(n):
        node = G[n]
        if node[0] == '"': return node[1]
        if add_loops and n == '8': 
            return dfs("42") + '+'
        if add_loops and n == '11':
            return f'(?P<self>{dfs("42")}(?&self)?{dfs("31")})'
        
        branch = lambda branch: ''.join(dfs(x) for x in branch.split())
        branches = map(branch, node.split('|'))
        return '(' + '|'.join(branches) + ')'

    return '^' + dfs('0') + '$'

def count_matches(rule, messeages): 
    return sum(bool(regex.match(rule, m)) for m in messeages.splitlines()) 

TEST_RULES = '''\
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"'''

TEST_MESSAGES = '''
ababbb
bababa
abbbab
aaabbb
aaaabbb'''

if __name__ == '__main__':
    assert count_matches(parse(TEST_RULES), TEST_MESSAGES) == 2
    rules, messeages = open('data/day19_test.in').read().split('\n\n')
    assert count_matches(parse(rules, add_loops=True), messeages) == 12

    rules, messeages = open('data/day19.in').read().split('\n\n')
    print(count_matches(parse(rules), messeages))
    print(count_matches(parse(rules, add_loops=True), messeages))
