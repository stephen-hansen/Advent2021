import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from collections import defaultdict, Counter
from functools import reduce
from utils import *
import copy

def merge_wins(win1, win2):
    win1[1] += win2[1]
    win1[2] += win2[2]
    return win1

@lru_cache(maxsize=None)
def game(p1, p2, sc1, sc2, turn, rollnum):
    wins = {1: 0, 2: 0}
    if turn == 2 and rollnum == 0 and sc1 >= 21:
        wins[1] += 1
    elif turn == 1 and rollnum == 0 and sc2 >= 21:
        wins[2] += 1
    else:
        for roll in range(3):
            if turn == 1:
                p1_, sc1_ = advance(roll+1, p1, sc1)
                rollnum_ = rollnum + 1
                turn_ = 1
                if rollnum_ == 3:
                    rollnum_ = 0
                    turn_ = 2
                else:
                    sc1_ = sc1
                wins = merge_wins(wins, game(p1_, p2, sc1_, sc2, turn_, rollnum_))
            else:
                p2_, sc2_ = advance(roll+1, p2, sc2)
                rollnum_ = rollnum + 1
                turn_ = 2
                if rollnum_ == 3:
                    rollnum_ = 0
                    turn_ = 1
                else:
                    sc2_ = sc2
                wins = merge_wins(wins, game(p1, p2_, sc1, sc2_, turn_, rollnum_))
    return wins

def advance(die, place, score):
    place_base10 = place - 1
    place_base10 += die
    if place_base10 >= 10:
        place_base10 %= 10
    place = place_base10 + 1
    score += place
    return place, score

def main():
    A = getlines_map_regex("Player . starting position: (.*)")
    p1 = int(A[0].group(1))
    p2 = int(A[1].group(1))
    sc1 = 0
    sc2 = 0
    wins = game(p1, p2, sc1, sc2, 1, 0)
    most_wins = max(wins[1], wins[2])
    p(most_wins)

if __name__ == "__main__":
    main()

