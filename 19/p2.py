import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from collections import defaultdict, Counter
from functools import reduce
from utils import *
import copy

def correct_orientation(sc, o=None):
    if o is None:
        o = ['x', 0]
    scans = []
    dr = o[0]
    up = o[1]
    for b in sc:
        x=b[0]
        y=b[1]
        z=b[2]
        s = [x,y,z]
        if dr == 'x':
            s = [x,y,z]
        elif dr == '-x':
            s = [-x,y,-z]
        elif dr == 'y':
            s = [-y,x,z]
        elif dr == '-y':
            s = [-y,-x,-z]
        elif dr == 'z':
            s = [-z,y,x]
        elif dr == '-z':
            s = [z,y,-x]
        for _ in range(up):
            if 'x' in dr:
                s[1], s[2] = s[2], -s[1]
            elif 'y' in dr:
                s[0], s[2] = s[2], -s[0]
            elif 'z' in dr:
                s[0], s[1] = s[1], -s[0]
        scans.append(s)
    return scans

def overlap(sc1, sc2, p1=None, o1=None):
    if p1 is None:
        p1 = [0,0,0]
    dirs = ['x','-x','y','-y','z','-z']
    abs_locs = []
    scans = correct_orientation(sc1, o1)
    for sc in scans:
        abs_locs.append([p1[0]+sc[0],p1[1]+sc[1],p1[2]+sc[2]])
    for d in dirs:
        for up in range(4):
            orientation = [d, up]
            scans2 = correct_orientation(sc2, orientation)
            for loc in abs_locs:
                for sc in scans2:
                    loc_estimate = [loc[0]-sc[0], loc[1]-sc[1], loc[2]-sc[2]]
                    abs_locs2 = []
                    for scan2 in scans2:
                        abs_locs2.append([loc_estimate[0]+scan2[0], loc_estimate[1]+scan2[1], loc_estimate[2]+scan2[2]])
                    num_matches = len(list(filter(lambda x: x in abs_locs, abs_locs2)))
                    if num_matches >= 12:
                        return True, loc_estimate, orientation
    return False, None, None

def main():
    A = getlines()
    scs = []
    sc = []
    for l in A:
        if len(l) == 0:
            scs.append(sc)
            sc = []
        elif not l.startswith('---'):
            nums = list(map(int, l.split(',')))
            sc.append(nums)
    scs.append(sc)
    locs = {0: [0,0,0]}
    ors = {0: ['x', 0]}
    tested = set()
    while len(locs) < len(scs):
        for i, sc1 in enumerate(scs):
            for j, sc2 in enumerate(scs):
                if (i,j) in tested:
                    continue
                if i == j:
                    continue
                if i in locs and j not in locs:
                    p("Testing i=" + str(i) + " vs j=" + str(j))
                    tested.add((i,j))
                    match, loc, orient = overlap(sc1, sc2, locs[i], ors[i])
                    if match:
                        locs[j] = loc
                        ors[j] = orient
    p("Done")
    farthest_dist = 0
    for i, l1 in locs.items():
        for j, l2 in locs.items():
            if i == j:
                continue
            dist = abs(l1[0] - l2[0]) + abs(l1[1] - l2[1]) + abs(l1[2] - l2[2])
            if dist > farthest_dist:
                farthest_dist = dist
    p(farthest_dist)

if __name__ == "__main__":
    main()

