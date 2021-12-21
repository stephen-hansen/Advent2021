import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from collections import defaultdict, Counter
from functools import reduce
from utils import *
import copy

def roll(die):
    die[0] += 1
    die[1] += 1
    if die[0] == 101:
        die[0] = 1
    return die

def advance(die, place, score):
    place_base10 = place - 1
    for _ in range(3):
        die = roll(die)
        place_base10 += die[0]
        if place_base10 >= 10:
            place_base10 %= 10
    place = place_base10 + 1
    score += place
    return die, place, score

def main():
    A = getlines_map_regex("Player . starting position: (.*)")
    p1 = int(A[0].group(1))
    p2 = int(A[1].group(1))
    sc1 = 0
    sc2 = 0
    die = [0, 0]
    win = None
    while True:
        die, p1, sc1 = advance(die, p1, sc1)
        if sc1 >= 1000:
            win = 1
            break
        die, p2, sc2 = advance(die, p2, sc2)
        if sc2 >= 1000:
            win = 2
            break
    losescore = 0
    if win == 1:
        losescore = sc2
    else:
        losescore = sc1
    p(losescore * die[1])

if __name__ == "__main__":
    main()

