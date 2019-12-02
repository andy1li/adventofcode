# https://adventofcode.com/2018/day/7

from collections import defaultdict
from graphviz import Graph
import re

def parse(input): 
    PATTERN = 'Step ([A-Z]) must be finished before step ([A-Z]) can begin.'
    G, tasks, vis = defaultdict(set), set(), Graph()
    for line in input:
        a, b = pair = re.match(PATTERN, line).groups()
        G[b].add(a); vis.edge(a, b)
        tasks |= set(pair)
    # print(G); #vis.view('day07')
    return G, sorted(tasks)

def fst_star(G, tasks): 
    steps = ''
    while len(steps) < len(tasks):
        for task in tasks:
            if (task not in steps 
            and all(dep in steps for dep in G[task])):
                steps += task; break
    return steps

def snd_star(G, steps, num_workers=5, base=60):
    t, workers, started, done = -1, set(), set(), ''

    while len(done) < len(steps):
        # Check tasks
        for fin_t, task in list(workers):
            if t == fin_t:
                done += task
                workers.discard((t, task))

        # Try to assign tasks
        for task in steps:
            if (len(workers) < num_workers
            and task not in started
            and all(dep in done for dep in G[task])):
                fin_t = t + ord(task)-ord('A')+1 + base
                workers.add((fin_t, task))
                started.add(task)
        # print(t, workers)
        t += 1
    return t
    
TEST = '''Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.'''.split('\n')

if __name__ == '__main__':
    G, tasks = parse(TEST)
    assert fst_star(G, tasks) == 'CABDFE'
    assert snd_star(G, fst_star(G, tasks), 2, 0) == 15

    G, tasks = parse(open('data/day07.in'))
    print(fst_star(G, tasks))
    print(snd_star(G, fst_star(G, tasks)))