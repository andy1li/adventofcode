# https://adventofcode.com/2019/day/22

from collections import deque

def deal_with(cards, size, n):
    i, new_cards = 0, [0]*size
    while cards:
        new_cards[i] = cards.popleft()
        i = (i+n) % size
    return deque(new_cards)

def shuffle(techs, size):
    cards = deque(range(size)) 
    for tech in techs:
        if tech.startswith('deal into'):
            cards.reverse()
        if tech.startswith('cut'):
            n = int(tech.split().pop())
            cards.rotate(-n)
        if tech.startswith('deal with'):
            n = int(tech.split().pop())
            cards = deal_with(cards, size, n)
    return list(cards)

def snd_star(data): 
    pass

TEST1 = '''deal with increment 7
deal into new stack
deal into new stack'''.split('\n')
TEST2 = '''cut 6
deal with increment 7
deal into new stack'''.split('\n')
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

    techs = open('data/day22.in')
    print(shuffle(techs, 10007).index(2019))
    # print(shuffle(techs, 119315717514047).index(2019))