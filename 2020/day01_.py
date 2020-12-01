# https://adventofcode.com/2020/day/1

from functools import reduce
from itertools import product
from operator  import mul

def product_sum_2020(nums, n): 
    for _tuple in product(nums, repeat=n):
        if sum(_tuple) == 2020:
            return reduce(mul, _tuple)

if __name__ == '__main__':
    nums = [*map(int, open('data/day01.in'))]
    print(product_sum_2020(nums, 2))
    print(product_sum_2020(nums, 3))