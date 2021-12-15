import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from collections import defaultdict, Counter
from functools import reduce
from utils import *
import copy

def main():
    A = getlines()
    G = Graph()
    for i in range(len(A)*5):
        for j in range(len(A[0])*5):
            key = (i, j)
            G.add_node(key)
    for i in range(len(A)*5):
        for j in range(len(A[0])*5):
            key = (i, j)
            neighbors = filter(lambda y: y[0] >= 0 and y[0] < len(A)*5 and y[1] >= 0 and y[1] < len(A[0])*5, map(lambda x: (key[0]+x[0],key[1]+x[1]), [(-1,0),(1,0),(0,-1),(0,1)]))
            orig_key = (i % len(A), j % len(A[0]))
            val = A[orig_key[0]][orig_key[1]]
            weight = int(val)
            incr = (i // len(A)) + (j // len(A[0]))
            for _ in range(incr):
                weight += 1
                if weight == 10:
                    weight = 1
            for n in neighbors:
                G.add_edge(n, key, weight)
    dist, prev = G.dijkstra((0, 0), (5*len(A)-1, 5*len(A[0])-1))
    best = dist[(5*len(A)-1, 5*len(A[0])-1)]
    p(best)

if __name__ == "__main__":
    main()

