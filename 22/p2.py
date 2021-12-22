import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from collections import defaultdict, Counter
from functools import reduce
from utils import *
import copy

def remove_intersection(r, i):
    new_cubes = []
    xdims = [[i[0][0], i[0][1]]]
    ydims = [[i[1][0], i[1][1]]]
    zdims = [[i[2][0], i[2][1]]]
    dims = [xdims, ydims, zdims]
    for k in range(3):
        # mins
        if i[k][0] > r[k][0]:
            dims[k].append([r[k][0], i[k][0]-1])
        # maxs
        if i[k][1] < r[k][1]:
            dims[k].append([i[k][1]+1, r[k][1]])
    for xdim in dims[0]:
        for ydim in dims[1]:
            for zdim in dims[2]:
                new_cubes.append([xdim, ydim, zdim])
    # Remove the intersection itself
    new_cubes.remove(i)
    return new_cubes

def main():
    A = getlines_map_regex("(.*) x=(.*)\.\.(.*),y=(.*)\.\.(.*),z=(.*)\.\.(.*)")
    on_regions = [] # List of cubes
    for l in A:
        p(l)
        turn_on = l.group(1) == "on"
        xmin = int(l.group(2))
        xmax = int(l.group(3))
        ymin = int(l.group(4))
        ymax = int(l.group(5))
        zmin = int(l.group(6))
        zmax = int(l.group(7))
        curr_region = [[[xmin, xmax], [ymin, ymax], [zmin, zmax]]]
        new_regions = []
        # if turn on, we need to remove intersections from curr_region, then add new area
        # if turn off, we just remove the intersections from the on_regions
        for region in on_regions:
            xmin_ = region[0][0]
            xmax_ = region[0][1]
            ymin_ = region[1][0]
            ymax_ = region[1][1]
            zmin_ = region[2][0]
            zmax_ = region[2][1]
            new_curr_region = []
            no_intersections = True
            for region2 in curr_region:
                xmin2_ = region2[0][0]
                xmax2_ = region2[0][1]
                ymin2_ = region2[1][0]
                ymax2_ = region2[1][1]
                zmin2_ = region2[2][0]
                zmax2_ = region2[2][1]
                intersects = (xmax2_ >= xmin_ and xmin2_ <= xmax_ and \
                        ymax2_ >= ymin_ and ymin2_ <= ymax_ and \
                        zmax2_ >= zmin_ and zmin2_ <= zmax_)
                if intersects:
                    no_intersections = False
                    intersection = [[max(xmin2_, xmin_), min(xmax2_, xmax_)],
                            [max(ymin2_, ymin_), min(ymax2_, ymax_)],
                            [max(zmin2_, zmin_), min(zmax2_, zmax_)]]
                    if not turn_on:
                        # Replace region with region w/o intersection
                        # Assume we don't break up curr region here, so one single region
                        modified_regions = remove_intersection(region, intersection)
                        for r in modified_regions:
                            new_regions.append(r)
                    else:
                        # Replace region2 with region w/o intersection
                        # here we do break it up
                        modified_regions = remove_intersection(region2, intersection)
                        for r in modified_regions:
                            new_curr_region.append(r)
                if not turn_on or not intersects:
                    # No change to curr region
                    new_curr_region.append(region2)
            if turn_on or no_intersections:
                # No change to region
                new_regions.append(region)
            curr_region = new_curr_region
        # Merge in new regions to turn on
        if turn_on:
            for region in curr_region:
                new_regions.append(region)
        on_regions = new_regions
    vol = 0
    for cube in on_regions:
        vol += abs(cube[0][1]+1 - cube[0][0])*abs(cube[1][1]+1 - cube[1][0])*abs(cube[2][1]+1 - cube[2][0])
    p(vol)

if __name__ == "__main__":
    main()

