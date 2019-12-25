# https://adventofcode.com/2019/day/22

from sympy import Poly, Symbol, simplify
import numpy as np

def mod_inverse(d, m):
    if m & 1:
        return pow(d, m-2, m) 
    else:
        return next(filter(
            lambda i: (d * i) % m == 1, range(m)
        )) 

def get_coeffs(techs, size):
    equation = Symbol("i")
    for tech in reversed(techs):
        if tech.startswith('deal into'):
            equation = size-1 - equation
        else:
            n = int(tech.split().pop())
            if tech.startswith('deal with'):
                equation *= mod_inverse(n, size)
            elif tech.startswith('cut'):
                equation += n

    equation = simplify(equation)
    coeffs = Poly(equation).all_coeffs()
    return np.array(coeffs) % size

def shuffle(techs, size):
    # x = step * i + start
    step, start = get_coeffs(techs, size)   
    deck = np.arange(size) 
    return list((step * deck + start) % size) 

def slam_shuffle(techs, size, n, i):
    step, start = get_coeffs(techs, size)
    step_to_n = pow(step, n, size)
    geom_series = (1 - step_to_n) * mod_inverse(1 - step, size) 
    return (step_to_n * i + geom_series * start) % size

TEST1 = '''deal with increment 7
deal into new stack
deal into new stack'''.splitlines()
TEST2 = '''cut 6
deal with increment 7
deal into new stack'''.splitlines()
TEST3 = '''deal with increment 7
deal with increment 9
cut -2'''.split('\n')
TEST4 = '''deal into new stack
cut -2
deal with increment 7
cut 8
cut -4
deal with increment 7
cut 3
deal with increment 9
deal with increment 3
cut -1'''.split('\n')

if __name__ == '__main__':
    assert shuffle(TEST1, 10) == [0,3,6,9,2,5,8,1,4,7]
    assert shuffle(TEST2, 10) == [3,0,7,4,1,8,5,2,9,6]
    assert shuffle(TEST3, 10) == [6,3,0,7,4,1,8,5,2,9]
    assert shuffle(TEST4, 10) == [9,2,5,8,1,4,7,0,3,6]

    techs = open('data/day22.in').readlines()
    print(shuffle(techs, 10007).index(2019))
    assert slam_shuffle(techs, size=10007, n=1, i=4703) == 2019
    print( slam_shuffle(techs, size=119315717514047, n=101741582076661, i=2020) )