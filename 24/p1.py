import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from collections import defaultdict, Counter
from functools import reduce
from utils import *
import copy

def calc_helper(steps, stack=None, k=0):
    if stack is None or len(stack) == 0:
        stack = [0]
    if len(steps) == 0:
        return True, 0
    step = steps[0]
    will_push = step[0]
    A = step[1]
    B = step[2]
    x = stack[0] + A
    if not will_push:
        stack.pop(0)
    for w in range(9, 0, -1):
        if will_push:
            if x != w:
                st = copy.deepcopy(stack)
                st.insert(0, w+B)
                result, number = calc_helper(steps[1:], st, k+1)
                if result:
                    return result, int(str(w) + str(number))
        else:
            if x == w:
                st = copy.deepcopy(stack)
                result, number = calc_helper(steps[1:], st, k+1)
                if result:
                    return result, int(str(w) + str(number))
    return False, 0

def calc(steps):
    _, number = calc_helper(steps)
    return number//10

def solve(lines):
    steps = []
    will_push = False
    A = 0
    B = 0
    prevline = False
    for l in lines:
        cmd = l[0]
        if cmd == 'inp':
            prevline = False
            continue
        adr1 = l[1]
        adr2 = l[2]
        if cmd == 'add' and adr1 == 'y' and adr2 == 'w':
            prevline = True
        else:
            if cmd == 'div' and adr1 == 'z':
                will_push = (adr2 == '1')
            elif cmd == 'add' and adr1 == 'x' and adr2 != 'z':
                A = int(adr2)
            elif cmd == 'add' and adr1 == 'y' and prevline:
                B = int(adr2)
                steps.append((will_push, A, B))
            prevline = False
    p(steps)
    return calc(steps)

def main():
    A = getlines_getsv(' ')
    result = solve(A)
    p(result)

if __name__ == "__main__":
    main()

