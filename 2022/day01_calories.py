# https://adventofcode.com/2022/day/1

def parse_foods(elf):
    return [*map(int, elf.split())]

def parse_elves(raw):
    return [*map(parse_foods, raw.read().split('\n\n'))]
    
def fst_star(elves): 
    return max(map(sum, elves))

def snd_star(elves):
    top_tree = sorted(map(sum, elves), reverse=True)[:3]
    return sum(top_tree)

if __name__ == '__main__':
    elves = parse_elves(open('data/day01.in'))
    print(fst_star(elves))
    print(snd_star(elves))