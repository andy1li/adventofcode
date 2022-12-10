# https://adventofcode.com/2022/day/10

from itertools import chain, accumulate

Program = list[int]

def parse_program(raw) -> Program:
    def parse_instruction(instruction: str):
        chunk = [0]
        if instruction.startswith('addx'):
            chunk += int(instruction.split()[1]),
        return chunk
    return [1] + list(chain.from_iterable(map(parse_instruction, raw)))

def run(program: Program):
    return enumerate(accumulate(program), 1)
   
def fst_star(program: Program): 
    return sum( i * x 
        for i, x in run(program) 
        if i in [20, 60, 100, 140, 180, 220]
    )

def snd_star(program: Program):
    screen = [
        '🟥' if abs((i-1) % 40 - x) < 2 else '⬜️️'
        for i, x in run(program)
    ]
    return [''.join(screen[i:i+40]) for i in range(0, 240, 40)]

TEST = '''\
noop
addx 3
addx -5'''.splitlines()

if __name__ == '__main__':
    # print(*run(parse_program(TEST)))

    program = parse_program(open('data/day10_test.in'))
    assert fst_star(program) == 13140
    # print(*snd_star(program), sep='\n', end='\n\n')

    program = parse_program(open('data/day10.in'))
    print(fst_star(program))
    print(*snd_star(program), sep='\n', end='\n\n')