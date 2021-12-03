import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from collections import defaultdict
from utils import *

def main():
    A = getlines()
    bits = {}
    for l in A:
        for i, c in enumerate(l):
            if i not in bits:
                bits[i] = {0: 0, 1: 0}
            bits[i][int(c)] += 1
    gamma = ''
    eps = ''
    for i in bits:
        if bits[i][0] > bits[i][1]:
            gamma += '0'
            eps += '1'
        else:
            gamma += '1'
            eps += '0'
    g = int(gamma, 2)
    e = int(eps, 2)

    p(g*e)

if __name__ == "__main__":
    main()

