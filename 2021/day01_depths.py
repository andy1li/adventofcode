# https://adventofcode.com/2021/day/1

def snd_star(depths):
    return [
        a + b + c
        for a, b, c in zip(depths, depths[1:], depths[2:])
    ]

def fst_star(depths): 
    return sum(
        (b - a) > 0
        for a, b in zip(depths, depths[1:])
    )

if __name__ == '__main__':
    depths = [*map(int, open('data/day01.in'))]
    print(fst_star(depths))
    print(fst_star(snd_star(depths)))