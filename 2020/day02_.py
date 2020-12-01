# https://adventofcode.com/2020/day/2

def fst_star(masses): 
    return sum(m//3-2 for m in masses)

def snd_star(masses):
    return sum(map(rec, masses))

if __name__ == '__main__':
    masses = [*map(int, open('data/day01.in'))]
    print(fst_star(masses))
    print(snd_star(masses))