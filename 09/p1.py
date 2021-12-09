import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from collections import defaultdict
from functools import reduce
from utils import *
import copy

def main():
    A = getlines()
    c = 0
    j = 0
    for l in A:
        low_points = [i for i in range(len(l)) if ((i >=1 and l[i] < l[i-1]) or i == 0) and ((i < len(l)-1 and l[i] < l[i+1]) or i == len(l)-1) and ((j >= 1 and l[i] < A[j-1][i]) or j == 0) and ((j < len(A)-1 and l[i] < A[j+1][i]) or j == len(A) - 1)]
        k = []
        for i in low_points:
            k.append(int(l[i]))
            rl = int(l[i]) + 1
            c += rl
        j += 1
    p(c)

if __name__ == "__main__":
    main()

