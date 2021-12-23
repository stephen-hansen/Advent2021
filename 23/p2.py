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
  #1#2#3#4#
  #1#2#3#4#
  #########

# labels
# i=0..3 r1
# i=4..7 r2
# i=8..11 r3
# i=12..15 r4
# i=16..22 h1-7

MEMO = set()

def get_steps(label, movfrom, movto):
    steps = 2 # Initial move out of spot and move into tile
    checks = [label[movto]]
    if movfrom > movto:
        # Hallway to room is inverse
        movto, movfrom = movfrom, movto
    # Compute path and step length
    # Extra step if moving from bottom room
    steps += movfrom % 4
    if movto <= 17: # h1, h2
        # 16 requires extra step and one extra check
        if movto == 16:
            steps += 1
            checks.append(label[17])
        for k in range(3):
            if movfrom >= 4*(k+1):
                steps += 2
                checks.append(label[18+k])
    elif movto == 18: # h3
        for k in range(2):
            if movfrom >= 4*(k+2):
                steps += 2
                checks.append(label[19+k])
    elif movto == 19: # h4 (mid)
        if movfrom <= 3:
            steps += 2
            checks.append(label[18])
        elif movfrom >= 12:
            steps += 2
            checks.append(label[20])
    elif movto == 20: # h5
        for k in range(2):
            if movfrom < 4*(k+1):
                steps += 2
                checks.append(label[18+k])
    elif movto >= 21: # h6, h7
        if movto == 22:
            steps += 1
            checks.append(label[21])
        for k in range(3):
            if movfrom < 4*(k+1):
                steps += 2
                checks.append(label[18+k])
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

@lru_cache(maxsize=None)
def generate_graph(label):
    global GRAPH
    if label in MEMO:
        return
    MEMO.add(label)
    if label not in GRAPH:
        GRAPH.add_node(label)
    # Moves to hallway
    char = 'AAAABBBBCCCCDDDD'
    for movfrom in range(0, 16, 4):
        ch = char[movfrom]
        og_movfrom = movfrom
        while label[movfrom] == '.' and movfrom - og_movfrom < 4:
            movfrom += 1
        should_continue = False
        if label[movfrom] == ch:
            should_continue = True
            movfromi = movfrom
            while movfromi - og_movfrom < 4:
                if label[movfromi] != '.' and label[movfromi] != ch:
                    should_continue = False
                    break
                movfromi += 1
        if should_continue or movfrom-og_movfrom >= 4 or label[movfrom] == '.':
            # Correct item, don't move
            continue
        # Find hallway to swap with
        for movto in range(16, 23):
            get_steps_and_update(label, movfrom, movto)
    # Moves to room
    room_nums = {'A': 3, 'B': 7, 'C': 11, 'D': 15}
    for movfrom in range(16, 23):
        user = label[movfrom]
        if user == '.':
            continue
        og_movto = room_nums[user]
        movto = og_movto
        continue_loop = False
        while og_movto - movto < 4 and label[movto] != '.':
            if label[movto] == user:
                movto -= 1
            else:
                continue_loop = True
                break
        if og_movto - movto >= 4 or continue_loop:
            continue
        get_steps_and_update(label, movfrom, movto)

def main():
    # TODO efficient graph representation of problem
    A = getlines()
    start = A[2][3] + 'DD' + A[3][3] + A[2][5] + 'CB' + A[3][5] + A[2][7] + 'BA' + A[3][7] + A[2][9] + 'AC' + A[3][9] + "."*7
    p(start)
    generate_graph(start)
    # TODO run dijkstra from start to finish state
    finish = "AAAABBBBCCCCDDDD" + "."*7
    dist, prev = GRAPH.dijkstra(start, finish)
    p(dist[finish])

if __name__ == "__main__":
    main()

