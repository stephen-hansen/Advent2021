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
    for i in range(-rows, 2*rows):
        for j in range(-cols, 2*cols):
            if (i,j) not in img:
                img[(i,j)] = '.'
    # Infinite
    for r in range(2):
        output_img = {}
        for tup, pixel in img.items():
            i = tup[0]
            j = tup[1]
            neighbors = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]
            value = 0
            for n in neighbors:
                newp = (i+n[0], j+n[1])
                if newp not in img:
                    if r == 0:
                        c = 0
                    else:
                        index = 0
                        ch = '.'
                        for _ in range(r):
                            ch = img_enh[index]
                            if ch == '#':
                                index = int("111111111", 2)
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

