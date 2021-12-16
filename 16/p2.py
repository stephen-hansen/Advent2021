import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from collections import defaultdict, Counter
from functools import reduce
from utils import *
import copy

def parse_packet(b):
    goal = 0
    i = 0
    version = int(b[0:3], 2)
    p(f"Version = {version}")
    type_id = int(b[3:6], 2)
    if type_id == 4:
        p("Literal")
        # Literal
        lit_val = ''
        i = 6
        while True:
            c = b[i]
            i += 1
            lit_val += b[i:i+4]
            i += 4
            if c == '0':
                break
        goal = int(lit_val, 2)
    else:
        p("Operator")
        # Operator
        length_type_id = b[6]
        bit_length = None
        sub_packets = None
        length = 0
        n_pkt = 0
        first_value = None
        if type_id == 0:
            goal = 0
        elif type_id == 1:
            goal = 1
        elif type_id == 2:
            goal = None
        elif type_id == 3:
            goal = None

        if length_type_id == '0':
            # Total bit length
            bit_length = int(b[7:22], 2)
            i = 22
        else:
            # Number of sub-packets
            sub_packets = int(b[7:18], 2)
            i = 18
        while (bit_length is not None and length < bit_length) or \
                (sub_packets is not None and n_pkt < sub_packets):
            amt, prev_goal = parse_packet(b[i:])
            if type_id == 0:
                goal += prev_goal
            elif type_id == 1:
                goal *= prev_goal
            elif type_id == 2:
                if goal is None or prev_goal < goal:
                    goal = prev_goal
            elif type_id == 3:
                if goal is None or prev_goal > goal:
                    goal = prev_goal
            elif type_id == 5:
                if first_value is None:
                    first_value = prev_goal
                else:
                    goal = int(first_value > prev_goal)
            elif type_id == 6:
                if first_value is None:
                    first_value = prev_goal
                else:
                    goal = int(first_value < prev_goal)
            elif type_id == 7:
                if first_value is None:
                    first_value = prev_goal
                else:
                    goal = int(first_value == prev_goal)
            i += amt
            length += amt
            n_pkt += 1
    return i, goal # i is length, goal is whatever it is


def main():
    A = getlines()
    maps = {'0': '0000',
            '1': '0001',
            '2': '0010',
            '3': '0011',
            '4': '0100',
            '5': '0101',
            '6': '0110',
            '7': '0111',
            '8': '1000',
            '9': '1001',
            'A': '1010',
            'B': '1011',
            'C': '1100',
            'D': '1101',
            'E': '1110',
            'F': '1111'}
    binstrs = []
    for l in A:
        binstr = ''
        for c in l:
            binstr += maps[c]
        binstrs.append(binstr)
    goal = 0
    for b in binstrs:
        i, bgoal = parse_packet(b)
        goal += bgoal
    p(goal)

if __name__ == "__main__":
    main()

