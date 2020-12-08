# https://adventofcode.com/2020/day/7

from collections import defaultdict
import re

def parse(rules):
    G = defaultdict(set)
    for rule in rules:
        colors = re.findall(r'(\d )?([a-z]+ [a-z]+) bag', rule)
        G[colors[0][1]] |= set(colors[1:])
    G['no other'] # put 'no other' in G
    return G

def fst_star(G): 
    def contain_gold(color):
        return color == 'shiny gold' or any(
            contain_gold(x) for _, x in G[color]
        )
    return sum(map(contain_gold, G)) - 1

def snd_star(G):
    def count(color):
        if G[color] == {('', 'no other')}: return 1
        return 1 + sum( 
            int(n) * count(x) for n, x in G[color] 
        )
    return count('shiny gold') - 1

TEST1 = '''\
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.'''.splitlines()

TEST2 = '''\
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.'''.splitlines()

if __name__ == '__main__':
    assert fst_star(parse(TEST1)) == 4
    assert snd_star(parse(TEST1)) == 32
    assert snd_star(parse(TEST2)) == 126
    G = parse(open('data/day07.in'))
    print(fst_star(G))
    print(snd_star(G))