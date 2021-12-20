import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from collections import defaultdict, Counter
from functools import reduce
from utils import *
import copy

def main():
    A = getlines()
    img_enh = ''
    img = None
    mode = 0
    rows = 0
    cols = 0
    for l in A:
        if len(l) == 0:
            mode = 1
        else:
            if mode == 0:
                img_enh += l
            else:
                if img is None:
                    img = {}
                    cols = len(l)
                j = 0
                for c in l:
                    img[(rows, j)] = c
                    j += 1
                rows += 1
    # Infinite
    for r in range(50):
        p(r)
        minx = min(img.keys(), key=lambda x: x[0])[0]
        maxx = max(img.keys(), key=lambda x: x[0])[0]
        miny = min(img.keys(), key=lambda x: x[1])[1]
        maxy = max(img.keys(), key=lambda x: x[1])[1]
        output_img = {}
        for j in range(miny-1, maxy+2):
            img[(minx-1,j)] = '.' if r % 2 == 0 else '#'
            img[(maxx+1,j)] = '.' if r % 2 == 0 else '#'
        for i in range(minx-1, maxx+2):
            img[(i,miny-1)] = '.' if r % 2 == 0 else '#'
            img[(i,maxy+1)] = '.' if r % 2 == 0 else '#'
        for tup, pixel in img.items():
            i = tup[0]
            j = tup[1]
            neighbors = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]
            value = 0
            for n in neighbors:
                newp = (i+n[0], j+n[1])
                if newp not in img:
                    ch = '.'
                    if r % 2 == 1:
                        ch = '#'
                    c = (ch == '#')
                else:
                    c = (img[newp] == '#')
                value *= 2
                value += c
            output_img[(i,j)] = img_enh[value]
        img = output_img
    p(len(list(filter(lambda x: x == '#', img.values()))))
if __name__ == "__main__":
    main()

