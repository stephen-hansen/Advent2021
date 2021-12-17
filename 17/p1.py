import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from collections import defaultdict, Counter
from functools import reduce
from utils import *
import copy

def get_trajectory(xv, yv, xmin, xmax, ymin, ymax):
    xpos = 0
    ypos = 0
    max_ypos = 0
    while True:
        xpos += xv
        ypos += yv
        if ypos > max_ypos:
            max_ypos = ypos
        if xv > 0:
            xv -= 1
        elif xv < 0:
            xv += 1
        yv -= 1
        if xmin <= xpos <= xmax and ymin <= ypos <= ymax:
            return max_ypos, True
        elif xpos > xmax or ypos < ymin:
            return max_ypos, False

def find_trajectory(xmin, xmax, ymin, ymax):
    highest_height = -1
    for xv in range(0, 300):
        for yv in range(-300, 300):
            height, passes = get_trajectory(xv, yv, xmin, xmax, ymin, ymax)
            if not passes:
                continue
            if height > highest_height:
                highest_height = height
    p(highest_height)

def main():
    A = getlines_map_regex("target area: x=(.*)\.\.(.*), y=(.*)\.\.(.*)")
    xmin = int(A[0].group(1))
    xmax = int(A[0].group(2))
    ymin = int(A[0].group(3))
    ymax = int(A[0].group(4))
    find_trajectory(xmin, xmax, ymin, ymax)

if __name__ == "__main__":
    main()

