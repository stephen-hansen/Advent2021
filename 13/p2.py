import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from collections import defaultdict
from functools import reduce
from utils import *
import copy

def main():
    A = getlines()
    dots = set()
    for i, l in enumerate(A):
        if len(l) == 0:
            break
        point = tuple(map(int, l.split(',')))
        dots.add(point)
    folds_tmp = A[i+1:]
    folds = []
    for l in folds_tmp:
        x_y = l[11]
        dim = int(l.split('=')[1])
        folds.append((x_y, dim))
    for i, f in enumerate(folds):
        x_y = f[0]
        dim = f[1]
        new_dots = set()
        for point in dots:
            x = point[0]
            y = point[1]
            if x_y == 'y':
                if y >= dim:
                    y = dim*2 - y
            else:
                if x >= dim:
                    x = dim*2 - x
            new_dots.add((x, y))
        dots = new_dots
    matrix = []
    max_x = max([x[0] for x in dots])
    max_y = max([x[1] for x in dots])
    for y in range(max_y+1):
        m = []
        for x in range(max_x+1):
            m.append(" ")
        matrix.append(m)
    for point in dots:
        matrix[point[1]][point[0]] = "X"
    p("\n".join(["".join([str(x) for x in m]) for m in matrix]))

if __name__ == "__main__":
    main()

