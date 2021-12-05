import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from collections import defaultdict
from functools import reduce
from utils import *
import math
def main():
    grid = defaultdict(int)
    A = getlines_map_regex("(.*),(.*) -> (.*),(.*)")
    for l in A:
        x1 = int(l.group(1))
        y1 = int(l.group(2))
        x2 = int(l.group(3))
        y2 = int(l.group(4))
        diag = False
        if not (x1 == x2 or y1 == y2):
            diag = True
        xmin = min(x1, x2)
        xmax = max(x1, x2)
        ymin = min(y1, y2)
        ymax = max(y1, y2)
        if not diag:
            for x in range(xmin, xmax+1):
                for y in range(ymin, ymax+1):
                    grid[(x,y)] += 1
        else:
            x = xmin
            if x == x1:
                y = y1
                yend = y2
            else:
                y = y2
                yend = y1
            for x in range(xmin, xmax+1):
                grid[(x,y)] += 1
                if y > yend:
                    y -= 1
                else:
                    y += 1
    c = 0
    for k, v in grid.items():
        if v > 1:
            c += 1
    p(c)
if __name__ == "__main__":
    main()

