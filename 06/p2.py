import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from collections import defaultdict
from functools import reduce
from utils import *
import copy

MEM = {}

def total_spawns(fish, day):
    if (fish, day) in MEM:
        return MEM[(fish, day)]
    total = 0
    if day == 0:
        total = 1
    elif fish == 0:
        total = total_spawns(6, day-1) + total_spawns(8, day-1)
    else:
        total = total_spawns(fish-1, day-1)
    MEM[(fish, day)] = total
    return total

def main():
    l = [int(x) for x in getlines_getsv(',')[0]]
    #l = [3,4,3,1,2]
    total = 0
    for f in l:
        total += total_spawns(f, 256)
    p(total)

if __name__ == "__main__":
    main()

