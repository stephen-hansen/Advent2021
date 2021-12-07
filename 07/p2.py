import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from collections import defaultdict
from functools import reduce
from utils import *
import copy

def main():
    A = [int(x) for x in getlines_getsv(',')[0]]
    maxp = max(A)
    f = 0
    minf = 99999999
    minv = None
    for i in range(maxp):
        f = 0
        for c in A:
            n = abs(c-i)+1
            f += (n*(n-1))//2
        if f < minf:
            minf = f
            minv = i
    p(minf)

if __name__ == "__main__":
    main()

