import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from collections import defaultdict, Counter
from functools import reduce
from utils import *
import copy

def main():
    A = getlines()
    G = Graph()
    for i, line in enumerate(A):
        for j, val in enumerate(line):
            key = (i, j)
            G.add_node(key)
    for i, line in enumerate(A):
        for j, val in enumerate(line):
            key = (i, j)
            neighbors = filter(lambda y: y[0] >= 0 and y[0] < len(A) and y[1] >= 0 and y[1] < len(line), map(lambda x: (key[0]+x[0],key[1]+x[1]), [(-1,0),(1,0),(0,-1),(0,1)]))
            weight = int(val)
            for n in neighbors:
                G.add_edge(n, key, weight)
    dist, prev = G.dijkstra((0, 0))
    best = dist[(len(A)-1, len(A[0])-1)]
    p(best)

if __name__ == "__main__":
    main()

