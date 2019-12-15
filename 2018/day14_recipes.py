# https://adventofcode.com/2018/day/14

from tqdm import tqdm

def step(recipes, elves):
    s = recipes[elves[0]], recipes[elves[1]]
    digits = map(int, str(s[0] + s[1]))
    recipes.extend(digits)
    elves = [
        (elves[0] + s[0] + 1) % len(recipes),
        (elves[1] + s[1] + 1) % len(recipes),
    ]
    return recipes, elves

def fst_star(cutoff):
    recipes, elves = [3, 7], [0, 1]
    while len(recipes) <= cutoff + 10:
        recipes, elves = step(recipes, elves)
    return ''.join(map(str, recipes[cutoff:cutoff+10]))

def find(recipes, len_target, target):
    # print(recipes, target)
    fst_try = recipes[-len_target:] == target
    snd_try = recipes[-len_target-1:-1] == target
    
    if fst_try: return len(recipes) - len_target
    if snd_try: return len(recipes) - len_target - 1

def snd_star(target):
    target = [*map(int, str(target))]
    len_target = len(target)

    recipes, elves, t, i = [3, 7], [0, 1], tqdm(), 0
    while not find(recipes, len_target, target):
        recipes, elves = step(recipes, elves)
        i += 1; t.update()
 
    t.close()
    return find(recipes, len_target, target)

if __name__ == '__main__':
    assert fst_star(5) == '0124515891'
    # assert snd_star(51589) == 9
    # assert snd_star('01245') == 5
    # assert snd_star(92510) == 18
    # assert snd_star(59414) == 2018

    print(fst_star(505961))
    print(snd_star(505961))