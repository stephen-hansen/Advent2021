import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from collections import defaultdict, Counter
from functools import reduce
from utils import *
import copy

def main():
    A = getlines_map(list)
    moved = 0
    steps = 0
    while True:
        nextA = copy.deepcopy(A)
        moved = 0
        steps += 1
        for i in range(len(A)):
            for j in range(len(A[0])):
                c = A[i][j]
                if c == '>':
                    next_pos = A[i][(j+1)%len(A[0])]
                    if next_pos == '.':
                        moved += 1
                        nextA[i][j] = '.'
                        nextA[i][(j+1)%len(A[0])] = '>'
        A = nextA
        nextA = copy.deepcopy(A)
        for i in range(len(A)):
            for j in range(len(A[0])):
                c = A[i][j]
                if c == 'v':
                    next_pos = A[(i+1)%len(A)][j]
                    if next_pos == '.':
                        moved += 1
                        nextA[i][j] = '.'
                        nextA[(i+1)%len(A)][j] = 'v'
        A = nextA
        if moved == 0:
            break
    p(steps)
if __name__ == "__main__":
    main()

