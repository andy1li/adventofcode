# https://adventofcode.com/2020/day/19
# Originally from @TheLocehiliosan https://www.reddit.com/r/adventofcode/comments/kg1mro/2020_day_19_solutions/ggc1ozx

from lark import Lark, LarkError

def count_matches(rules, messages, add_loops=False):
    if add_loops: rules = ( rules
        .replace('8: 42', '8: 42 | 42 8')
        .replace('11: 42 31', '11: 42 31 | 42 11 31')
    )
    to_letters = str.maketrans('0123456789', 'abcdefghij')
    l = Lark(rules.translate(to_letters), start='a')
        
    def parse(message):
        try: return bool(l.parse(message))
        except LarkError: return False
    return sum(map(parse, messages.splitlines()))

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
    assert count_matches(TEST_RULES, TEST_MESSAGES) == 2
    rules, messeages = open('data/day19_test.in').read().split('\n\n')
    assert count_matches(rules, messeages, add_loops=True) == 12

    rules, messeages = open('data/day19.in').read().split('\n\n')
    print(count_matches(rules, messeages))
    print(count_matches(rules, messeages, add_loops=True))
