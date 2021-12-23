import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from collections import defaultdict, Counter
from functools import reduce
from utils import *
import copy

GRAPH = Graph()

#############
#12.3.4.5.67#
###1#2#3#4###
  #1#2#3#4#
  #########

# labels
# i=0 r1 top
# i=1 r1 bot
# i=2 r2 top
# i=3 r2 bot
# i=4 r3 top
# i=5 r3 bot
# i=6 r4 top
# i=7 r4 bot
# i=8..14 h1-7

MEMO = set()

def generate_graph(label):
    global GRAPH
    if label in MEMO:
        return
    MEMO.add(label)
    name_to_energy_per_step = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
    if label not in GRAPH:
        GRAPH.add_node(label)
    # Moves to hallway
    char = 'AABBCCDD'
    for movfrom in range(0, 8, 2):
        ch = char[i]
        if label[movfrom] == '.':
            # Top empty, only consider bottom
            movfrom += 1
        if label[movfrom] == ch or label[movfrom] == '.':
            # Correct item, don't  move
            continue
        # Find hallway to swap with
        for movto in range(8, 15):
            steps = 2 # Initial move out of room and move into tile
            checks = []
            checks.append(label[movto])
            # Compute path and step length
            # Extra step if moving from bottom room
            if movfrom % 2 == 1:
                steps += 1
            if movto <= 9:
                # 8 requires extra step and one extra check
                if movto == 8:
                    steps += 1
                    checks.append(label[9])
                for k in range(3):
                    if movfrom >= 2*(k+1):
                        steps += 2
                        checks.append(label[10+k])
            elif movto == 10: # h3
                for k in range(2):
                    if movfrom >= 2*(k+2):
                        steps += 2
                        checks.append(label[11+k])
            elif movto == 11: # h4 (mid)
                pass
            elif movto == 12: # h5
                pass
            elif movto >= 13: # h6, h7
                pass
            # Validate path is available
            for c in checks:
                if c != '.':
                    continue
            # Do the swap
            newlabel = copy.deepcopy(label)
            newlabel[movfrom] = '.'
            newlabel[movto] = label[movfrom]
            if newlabel not in GRAPH:
                GRAPH.add_node(newlabel)
            weight = steps * name_to_energy_per_step[label[movfrom]]
            GRAPH.add_edge(label, newlabel, weight)
            # Evaluate new node
            generate_graph(newlabel)
    # Moves to room
    for movfrom in range(8, 15):
        user = label[movfrom]
        if user == '.':
            continue

def main():
    # TODO efficient graph representation of problem
    A = getlines()
    start = A[2][4] + A[3][4] + A[2][6] + A[3][6] + A[2][8] + A[3][8] + A[2][10] + A[3][10] + "."*7
    generate_graph(start)
    # TODO run dijkstra from start to finish state
    finish = "AABBCCDD" + "."*7

if __name__ == "__main__":
    main()

