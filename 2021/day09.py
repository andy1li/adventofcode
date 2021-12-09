# https://adventofcode.com/2021/day/9

def parse(raw):
    command, x = raw.split()
    return int(x) * DIR[command]

def fst_star(commands): 
    pos = sum(commands)
    return int(pos.real * pos.imag) 

def snd_star(commands):
    pos = aim = 0
    for c in commands:
        if not c.real: aim += c
        else         : pos += c * (1 + aim)
    return int(pos.real * pos.imag) 

TEST = '''\
forward 5
down 5
forward 8
up 3
down 8
forward 2'''.splitlines()

if __name__ == '__main__':
    assert fst_star(map(parse, TEST)) == 150
    assert snd_star(map(parse, TEST)) == 900

    depths = list(map(parse, open('data/day09.in')))
    print(fst_star(depths))
    print(snd_star(depths))