# https://adventofcode.com/2019/day/22

import numpy as np

def mod_inverse(d, m): 
    return pow(d, m-2, m) 

def get_deck(techs, size):
    start, step = 0, 1
    for tech in techs:
        if tech.startswith('deal into'):
            step *= -1
            start = (start + step) % size

        if tech.startswith('cut'):
            n = int(tech.split().pop())
            start = (start + step * n) % size

        if tech.startswith('deal with'):
            n = int(tech.split().pop())
            if size % 2:
                step = (step * mod_inverse(n, size)) % size
            else:
                step = next( (j*size+step) // n
                    for j in range(size)
                    if (j*size+step) // n == (j*size+step) / n
                )
    return start, step

def shuffle(techs, size):
    start, step = get_deck(techs, size)   
    deck = np.arange(size) 
    return list((step * deck + start) % size) 

def slam_shuffle(techs, size, n, i):
    def geom_series(step):
        return (1 - step_to_n) * mod_inverse(1 - step, size) 

    start, step = get_deck(techs, size)
    step_to_n = pow(step, n, size)
    return (step_to_n * i + geom_series(step) * start) % size

TEST1 = '''deal with steprement 7
deal into new stack
deal into new stack'''.split('\n')
TEST2 = '''cut 6
deal with steprement 7
deal into new stack'''.split('\n')
TEST3 = '''deal with steprement 7
deal with steprement 9
cut -2'''.split('\n')
TEST4 = '''deal into new stack
cut -2
deal with steprement 7
cut 8
cut -4
deal with steprement 7
cut 3
deal with steprement 9
deal with steprement 3
cut -1'''.split('\n')

if __name__ == '__main__':
    assert shuffle(TEST1, 10) == [0,3,6,9,2,5,8,1,4,7]
    assert shuffle(TEST2, 10) == [3,0,7,4,1,8,5,2,9,6]
    assert shuffle(TEST3, 10) == [6,3,0,7,4,1,8,5,2,9]
    assert shuffle(TEST4, 10) == [9,2,5,8,1,4,7,0,3,6]

    techs = open('data/day22.in').readlines()
    print(shuffle(techs, 10007).index(2019))
    print(slam_shuffle(techs, 119315717514047, 101741582076661, 2020))
    