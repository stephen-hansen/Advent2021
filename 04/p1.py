import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from collections import defaultdict
from functools import reduce
from utils import *

def get_sum(board, ns, n):
    un_sum = 0
    win_sum = int(n)
    for r in board[:5]:
        print(r)
        for c in r:
            if c not in ns:
                un_sum += int(c)
    print(un_sum * win_sum)

def main():
    A = getlines()
    l1 = A[0]
    lines = A[2:]
    boards = []
    board = []
    for l in lines:
        if l == '':
            boards.append(board)
            board = []
        else:
            board.append(list(filter(lambda x: x != '', l.split(' '))))
    boards.append(board)
    ns = l1.split(',')

    better_boards = []
    for b in boards:
        nb = []
        for i in range(len(b[0])):
            nb.append(b[i])
        for i in range(len(b[0])):
            nb.append([x[i] for x in b])
        better_boards.append(nb)
    
    n_present = set()
    for n in ns:
        print(n)
        n_present.add(n)
        for b in better_boards:
            for r in b:
                match = True
                for c in r:
                    if c not in n_present:
                        match = False
                        break
                if match:
                    get_sum(b, n_present, n)
                    return


if __name__ == "__main__":
    main()

