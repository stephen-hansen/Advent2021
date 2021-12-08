import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from collections import defaultdict
from functools import reduce
from utils import *
import copy

def main():
    A = getlines_map_regex("(.*) \| (.*)")
    c = 0
    for l in A:
        signal_patterns = l.group(1).split(' ')
        output_val = l.group(2).split(' ')
        mappings = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
        mappings2 = {}
        for i in output_val:
            k = len(i)
            if k == 2 or k == 4 or k == 3 or k == 7:
                c += 1
    p(c)

if __name__ == "__main__":
    main()

