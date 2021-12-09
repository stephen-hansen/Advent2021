import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from collections import defaultdict
from functools import reduce
from utils import *
import copy

COUNTED = set()

def one_up(A, i, j):
    COUNTED.add((i, j))
    targ = int(A[j][i]) + 1
    neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
    s = 0
    if targ == 9:
        return 0
    for n in neighbors:
        i0, j0 = n
        if i0 < 0 or i0 >= len(A[0]) or j0 < 0 or j0 >= len(A):
            continue
        if int(A[j0][i0]) != 9 and (i0, j0) not in COUNTED:
            s += 1 + one_up(A, i0, j0)
    return s

def main():
    A = getlines()
    #A = ["2199943210", "3987894921", "9856789892", "8767896789", "9899965678"]
    c = 0
    j = 0
    k = []
    for l in A:
        low_points = [i for i in range(len(l)) if ((i >=1 and l[i] < l[i-1]) or i == 0) and ((i < len(l)-1 and l[i] < l[i+1]) or i == len(l)-1) and ((j >= 1 and l[i] < A[j-1][i]) or j == 0) and ((j < len(A)-1 and l[i] < A[j+1][i]) or j == len(A) - 1)]
        for i in low_points:
            basin = 1 + one_up(A, i, j)
            p(basin)
            p((i, j))
            p('---')
            if len(k) < 3:
                k.append(basin)
            elif basin > min(k):
                k.remove(min(k))
                k.append(basin)
        j += 1
    p(k)
    p(k[0] * k[1] * k[2])

if __name__ == "__main__":
    main()

