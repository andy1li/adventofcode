# https://adventofcode.com/2018/day/9

from collections import deque

def both_stars(num_players, last_score):
    scores, game = [0]*num_players, deque([0])

    for marble in range(1, last_score+1):
        if marble % 23:
            game.rotate(-2)
            game.appendleft(marble)
        else:
            player = (marble-1) % num_players
            game.rotate(7)
            scores[player] += marble + game.popleft()

    return max(scores)

if __name__ == '__main__':
    assert both_stars(17, 1104) == 2764

    print(both_stars(441, 71032))
    print(both_stars(441, 71032*100))
