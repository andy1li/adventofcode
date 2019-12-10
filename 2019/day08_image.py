# https://adventofcode.com/2019/day/8

from matplotlib import pyplot as plt

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
        if x != '2': return int(x)

def decode(data, width, height):
    data = parse(data, width, height)
    check(data)

    image = [*map(see, zip(*data))]
    image = [ image[i:i+width]
        for i in range(0, len(image), width)
    ]
    plt.imshow(image); plt.show()

if __name__ == '__main__':
    # decode('0222112222120000', 2, 2)
    decode(open('data/day08.in').read(), 25, 6)