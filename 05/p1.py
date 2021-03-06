import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from collections import defaultdict
from functools import reduce
from utils import *

def main():
    grid = defaultdict(int)
    A = getlines_map_regex("(.*),(.*) -> (.*),(.*)")
    for l in A:
        x1 = int(l.group(1))
        y1 = int(l.group(2))
        x2 = int(l.group(3))
        y2 = int(l.group(4))
        if not (x1 == x2 or y1 == y2):
            continue
        xmin = min(x1, x2)
        xmax = max(x1, x2)
        ymin = min(y1, y2)
        ymax = max(y1, y2)
        for x in range(xmin, xmax+1):
            for y in range(ymin, ymax+1):
                grid[(x,y)] += 1
    c = 0
    for k, v in grid.items():
        if v > 1:
            c += 1
    p(c)
if __name__ == "__main__":
    main()

