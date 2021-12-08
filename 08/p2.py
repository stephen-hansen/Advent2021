import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from collections import defaultdict
from functools import reduce
from utils import *
import copy

def main():
    A = getlines_map_regex("(.*) \| (.*)")
    c = 0
    for l in A:
        signal_patterns = l.group(1).split(' ')
        output_val = l.group(2).split(' ')
        mappings = {}
        mappings2 = {}
        for s in signal_patterns:
            s = ''.join(sorted(s))
            if s not in mappings2:
                k = len(s)
                if k == 2:
                    mappings[1] = s
                    mappings2[s] = 1
                elif k == 4:
                    mappings[4] = s
                    mappings2[s] = 4
                elif k == 3:
                    mappings[7] = s
                    mappings2[s] = 7
                elif k == 7:
                    mappings[8] = s
                    mappings2[s] = 8
        top_left_and_mid = [x for x in mappings[4] if x not in mappings[1]]
        for s in signal_patterns:
            s = ''.join(sorted(s))
            if s not in mappings2:
                k = len(s)
                check = [x for x in top_left_and_mid if x in s]
                check2 = [x for x in mappings[1] if x in s]
                if k == 6:
                    # 0, 6, or 9
                    # if 0, len(check) is 1, else it is 6 or 9
                    if len(check) == 1:
                        mappings[0] = s
                        mappings2[s] = 0
                    else:
                        if len(check2) == 1:
                            mappings[6] = s
                            mappings2[s] = 6
                        else:
                            mappings[9] = s
                            mappings2[s] = 9
                elif k == 5:
                    # 2, 3, or 5
                    # if 5, len(check) is 2, else it is 2 or 3
                    if len(check) == 2:
                        mappings[5] = s
                        mappings2[s] = 5
                    else:
                        if len(check2) == 1:
                            mappings[2] = s
                            mappings2[s] = 2
                        else:
                            mappings[3] = s
                            mappings2[s] = 3
        # Got em all
        num = 0
        for s in output_val:
            s = ''.join(sorted(s))
            number = mappings2[s]
            num *= 10
            num += number
        c += num
    p(c)

if __name__ == "__main__":
    main()

