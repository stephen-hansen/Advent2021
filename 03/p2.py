import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from collections import defaultdict
from utils import *
import copy

def main():
    A = getlines()
    bits = {'o':{0: 0, 1: 0}, 'c':{0: 0, 1: 0}}
    o = copy.deepcopy(A)
    c = copy.deepcopy(A)
    for i in range(len(A[0])):
        for n in bits['o']:
            bits['o'][n] = len(list(filter(lambda x: int(x[i]) == n, o)))
            bits['c'][n] = len(list(filter(lambda x: int(x[i]) == n, c)))
        if len(o) > 1:
            if bits['o'][0] <= bits['o'][1]:
                o = list(filter(lambda x: x[i] == '1', o))
            else:
                o = list(filter(lambda x: x[i] == '0', o))
        if len(c) > 1:
            if bits['c'][0] <= bits['c'][1]:
                c = list(filter(lambda x: x[i] == '0', c))
            else:
                c = list(filter(lambda x: x[i] == '1', c))
    p(c)
    p(o)
    p(int(c[0], 2)*int(o[0], 2))

if __name__ == "__main__":
    main()

