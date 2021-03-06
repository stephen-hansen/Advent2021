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

def get_steps(label, movfrom, movto):
    steps = 2 # Initial move out of spot and move into tile
    checks = [label[movto]]
    if movfrom > movto:
        # Hallway to room is inverse
        movto, movfrom = movfrom, movto
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
        if movfrom <= 1:
            steps += 2
            checks.append(label[10])
        elif movfrom >= 6:
            steps += 2
            checks.append(label[12])
    elif movto == 12: # h5
        for k in range(2):
            if movfrom < 2*(k+1):
                steps += 2
                checks.append(label[10+k])
    elif movto >= 13: # h6, h7
        if movto == 14:
            steps += 1
            checks.append(label[13])
        for k in range(3):
            if movfrom < 2*(k+1):
                steps += 2
                checks.append(label[10+k])
    # Validate path is available
    for c in checks:
        if c != '.':
            return None
    return steps

def get_steps_and_update(label, movfrom, movto):
    global GRAPH
    name_to_energy_per_step = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
    steps = get_steps(label, movfrom, movto)
    if steps is not None:
        newlabel = list(copy.deepcopy(label))
        newlabel[movfrom] = '.'
        newlabel[movto] = label[movfrom]
        newlabel = ''.join(newlabel)
        if newlabel not in GRAPH:
            GRAPH.add_node(newlabel)
        weight = steps * name_to_energy_per_step[label[movfrom]]
        GRAPH.add_edge(label, newlabel, weight)
        # Evaluate new node
        generate_graph(newlabel)

def generate_graph(label):
    global GRAPH
    if label in MEMO:
        return
    MEMO.add(label)
    if label not in GRAPH:
        GRAPH.add_node(label)
    # Moves to hallway
    char = 'AABBCCDD'
    for movfrom in range(0, 8, 2):
        ch = char[movfrom]
        if label[movfrom] == '.':
            # Top empty, only consider bottom
            movfrom += 1
        if label[movfrom] == ch or label[movfrom] == '.':
            # Correct item, don't  move
            continue
        # Find hallway to swap with
        for movto in range(8, 15):
            get_steps_and_update(label, movfrom, movto)
    # Moves to room
    room_nums = {'A': 1, 'B': 3, 'C': 5, 'D': 7}
    for movfrom in range(8, 15):
        user = label[movfrom]
        if user == '.':
            continue
        movto = room_nums[user]
        if label[movto] != '.':
            if label[movto] == user:
                movto -= 1
            else:
                continue
        get_steps_and_update(label, movfrom, movto)

def main():
    # TODO efficient graph representation of problem
    A = getlines()
    start = A[2][3] + A[3][3] + A[2][5] + A[3][5] + A[2][7] + A[3][7] + A[2][9] + A[3][9] + "."*7
    p(start)
    generate_graph(start)
    # TODO run dijkstra from start to finish state
    finish = "AABBCCDD" + "."*7
    dist, prev = GRAPH.dijkstra(start, finish)
    p(dist[finish])

if __name__ == "__main__":
    main()

