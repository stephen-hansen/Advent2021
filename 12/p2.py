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
    pdict = [{"start": 1}]
    doubl = [None]
    final = []
    while True:
        if len(paths) == 0:
            break
        path = paths.pop()
        dic = pdict.pop()
        og_dbl = doubl.pop()
        nxt = conns[path[-1]]
        if path[-1] == "end":
            final.append(path)
            continue
        for n in nxt:
            dbl = og_dbl
            if n == "start":
                continue
            if not n.isupper() and n in dic and dbl is not None:
                continue
            p2 = copy.deepcopy(path)
            p2.append(n)
            d2 = copy.deepcopy(dic)
            if n not in d2:
                d2[n] = 0
            d2[n] += 1
            paths.append(p2)
            pdict.append(d2)
            if not n.isupper() and d2[n] == 2:
                dbl = n
            doubl.append(dbl)
    p(len(final))

if __name__ == "__main__":
    main()

