# https://adventofcode.com/2019/day/21

from intcode import run

def run_script(code, script):
    bot = run(code, script)
    output = list(bot); damage = output.pop()
    print(bytes(output).decode().strip())
    print(damage)

if __name__ == '__main__':
    code = [*map(int, open('data/day21.in').read().split(','))]
    # jump if hole in 'ABC' and ground @ 'D' 
    script = b'''NOT A J
                 NOT B T
                 OR  T J
                 NOT C T
                 OR  T J
                 AND D J
                 WALK
    '''
    run_script(code, script); print()

    # jump if hole in 'ABC' and ground @ 'D' 
    # and can continue to [walk (ground @ 'E' ) or jump (ground @ 'H')]
    script = b'''NOT A J
                 NOT B T
                 OR  T J
                 NOT C T
                 OR  T J
                 AND D J
                 NOT E T
                 NOT T T
                 OR  H T
                 AND T J
                 RUN
    '''
    run_script(code, script)