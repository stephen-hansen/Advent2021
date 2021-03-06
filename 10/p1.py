import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from collections import defaultdict
from functools import reduce
from utils import *
import copy

def main():
    A = getlines()
    tot = 0
    sc = {')': 3, ']': 57, '}': 1197, '>': 25137}
    for l in A:
        stack = []
        corrupt = False
        for c in l:
            if c == '[':
                stack.append(']')
            elif c == '(':
                stack.append(')')
            elif c == '{':
                stack.append('}')
            elif c== '<':
                stack.append('>')
            else:
                top = stack.pop()
                if c != top:
                    corrupt = True
                    break
        if corrupt:
            tot += sc[c]
    p(tot)

if __name__ == "__main__":
    main()

