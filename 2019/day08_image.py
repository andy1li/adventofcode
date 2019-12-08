# https://adventofcode.com/2019/day/8

def parse(data, width, height):
    n = width * height
    return [ data[i:i+n]
        for i in range(0, len(data), n)
    ]

def check(data): 
    min_zero = min(data, key=lambda x: x.count('0'))
    print(min_zero.count('1') * min_zero.count('2'))

def see(pixel):
    for x in pixel:
        if x != '2': 
            return '⬛' if x=='0' else '⬜'

def decode(data, width, height):
    data = parse(data, width, height)
    check(data)

    image = [*map(see, zip(*data))]
    for i in range(0, len(image), width):
        print(''.join(image[i:i+width]))
    print()

if __name__ == '__main__':
    decode('0222112222120000', 2, 2)
    decode(open('data/day08.in').read(), 25, 6)