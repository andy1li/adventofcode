# https://adventofcode.com/2020/day/1

from functools import reduce
from itertools import combinations
from operator  import mul

def product_sum_2020(nums, n): 
    for tuple_ in combinations(nums, n):
        if sum(tuple_) == 2020:
            return reduce(mul, tuple_)

if __name__ == '__main__':
    nums = [*map(int, open('data/day01.in'))]
    print(product_sum_2020(nums, 2))
    print(product_sum_2020(nums, 3))