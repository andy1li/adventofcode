# https://adventofcode.com/2019/day/19

from bisect import bisect_left
from intcode import run
from itertools import product
from matplotlib import pyplot as plt
import numpy as np

def check(x, y):
    return next(run(code, [x, y]))

def scan(n=50):
    image = np.zeros([n, n], bool)
    for x, y in product(range(n), repeat=2):
        image[y, x] = check(x, y)
    # plt.imshow(image); plt.show()
    return image

def fst_star(): 
    return scan().sum()

def snd_star():
    class HundredByHundred: 
        def __getitem__(self, x):
            y = x
            while not check(x, y): y += 1
            return (check(x-99, y)    and check(x, y) 
                and check(x-99, y+99) and check(x, y+99)
            )

    y = x = bisect_left(HundredByHundred(), True, 1, 10**4)
    while not check(x, y): y += 1
    return (x-99) * 10000 + y

if __name__ == '__main__':
    code = [*map(int, open('data/day19.in').read().split(','))]
    print(fst_star())
    print(snd_star())