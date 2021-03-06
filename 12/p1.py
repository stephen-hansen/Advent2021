import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from collections import defaultdict
from functools import reduce
from utils import *
import copy

def main():
    A = getlines_map_regex("(.*)-(.*)")
    c = 0
    conns = {}
    for l in A:
        d0 = l.group(1)
        d1 = l.group(2)
        if d0 not in conns:
            conns[d0] = []
        if d1 not in conns:
            conns[d1] = []
        conns[d0].append(d1)
        conns[d1].append(d0)
    paths = [["start"]]
    final = []
    while True:
        if len(paths) == 0:
            break
        path = paths.pop()
        nxt = conns[path[-1]]
        if path[-1] == "end":
            final.append(path)
            continue
        for n in nxt:
            if not n.isupper() and n in path:
                continue
            p2 = copy.deepcopy(path)
            p2.append(n)
            paths.append(p2)
    p(len(final))

if __name__ == "__main__":
    main()

