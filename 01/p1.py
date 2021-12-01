import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import utils

def main():
    lines = utils.getlines_int()
    prev = None
    inc = 0
    for i in lines:
        if prev is not None:
            inc += int(i > prev)
        prev = i
    utils.p(inc)

if __name__ == "__main__":
    main()

