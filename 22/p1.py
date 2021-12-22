import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from collections import defaultdict, Counter
from functools import reduce
from utils import *
import copy

def main():
    A = getlines_map_regex("(.*) x=(.*)\.\.(.*),y=(.*)\.\.(.*),z=(.*)\.\.(.*)")
    on = set()
    for l in A:
        turn_on = l.group(1) == "on"
        xmin = int(l.group(2))
        xmax = int(l.group(3))
        ymin = int(l.group(4))
        ymax = int(l.group(5))
        zmin = int(l.group(6))
        zmax = int(l.group(7))
        if (xmin > 50) or (xmax < -50) or (ymin > 50) or (ymax < -50) or (zmin > 50) or (zmax < -50):
            continue
        for x in range(xmin, xmax+1):
            for y in range(ymin, ymax+1):
                for z in range(zmin, zmax+1):            
                    cube = (x,y,z)
                    if turn_on:
                        on.add(cube)
                    else:
                        if cube in on:
                            on.remove(cube)
    p(len(on))

if __name__ == "__main__":
    main()

