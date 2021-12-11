import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from collections import defaultdict
from functools import reduce
from utils import *
import copy

def main():
    A = getlines()
    c = 0
    A = [list(map(int, list(l))) for l in A]
    for k in range(99999999):
        flash_dict = set()
        flashes = []
        n_flashes = 0
        for i in range(len(A)):
            for j in range(len(A[i])):
                A[i][j] += 1
                if A[i][j] > 9 and (i, j) not in flash_dict:
                    flashes.append((i, j))
                    flash_dict.add((i, j))
        while True:
            if len(flashes) == 0:
                break
            i0, j0 = flashes.pop()
            n_flashes += 1
            adjacent = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
            for i1, j1 in adjacent:
                try:
                    if i0+i1 < 0 or i0+i1 >= len(A) or j0+j1 < 0 or j0+j1 >= len(A):
                        continue
                    A[i0+i1][j0+j1] += 1
                    coord = (i0+i1, j0+j1)
                    if coord not in flash_dict and A[i0+i1][j0+j1] > 9:
                        flash_dict.add(coord)
                        flashes.append(coord)
                except Exception as e:
                    continue
        if len(flash_dict) == len(A) * len(A[0]):
            p(k+1)
            exit(0)
        for i1, j1 in flash_dict:
            c+=1
            A[i1][j1] = 0


if __name__ == "__main__":
    main()

