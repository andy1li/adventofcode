# https://adventofcode.com/2022/day/7

from itertools import chain

class Node:
    def __init__(self, name, parent=None, size=0):
        self.name = name
        self.parent = parent
        self.size = size
        self.children = []

    def tally(self):
        if self.children: 
            self.size = sum(c.tally() for c in self.children)
        return self.size

    def sizes(self):
        yield from chain.from_iterable(
            c.sizes()
            for c in self.children
            if c.children
        )
        yield self.size

def parse_root(raw):
    curr = root = Node('/')
    for line in raw:
        if line == '$ cd /': continue
        elif line.startswith('$ cd '): 
            dst = line[5:]
            curr = (
                curr.parent 
                if dst == '..' else 
                next(c for c in curr.children if c.name == dst)
            )
        else:
            a, b = line.split()
            if a == 'dir' : curr.children += Node(b, curr),
            if a.isdigit(): curr.children += Node(b, curr, int(a)),
    root.tally()
    return root

def fst_star(root): 
    return sum(filter(lambda x: x <= 100000, root.sizes()))

def snd_star(root):
    target = root.size - 40000000
    return min(filter(lambda x: x >= target, root.sizes()))

TEST = '''\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k'''.splitlines()

if __name__ == '__main__':
    root = parse_root(TEST)
    assert fst_star(root) == 95437
    assert snd_star(root) == 24933642

    root = parse_root(open('data/day07.in').read().splitlines())
    print(fst_star(root))
    print(snd_star(root))