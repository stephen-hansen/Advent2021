import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from collections import defaultdict
from functools import reduce
from utils import *
import copy

def main():
    A = getlines()
    tot = 0
    sc = {')': 1, ']': 2, '}': 3, '>': 4}
    scores = []
    for l in A:
        tot = 0
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
        if not corrupt and len(stack) > 0:
            stack.reverse()
            for c in stack:
                tot *= 5
                tot += sc[c]
            scores.append(tot)
    winner = list(sorted(scores))
    winner = winner[len(winner)//2]
    p(winner)

if __name__ == "__main__":
    main()

