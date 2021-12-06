import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from collections import defaultdict
from functools import reduce
from utils import *
import copy

def main():
    l = [int(x) for x in getlines_getsv(',')[0]]
    for i in range(80):
        fish = copy.deepcopy(l)
        for j, k in enumerate(l):
            fish[j] = k - 1
            if fish[j] == -1:
                fish[j] = 6
                fish.append(8)
        l = fish
    p(len(l))

if __name__ == "__main__":
    main()

