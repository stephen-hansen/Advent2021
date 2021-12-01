import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import utils

def main():
    lines = utils.getlines_int()
    prev = 0
    win = [0,0,0]
    inc = 0
    for i in lines:
        total = sum(win)
        if prev >= 3:
            inc += int((total - win[0] + i) > total)
        win[0] = win[1]
        win[1] = win[2]
        win[2] = i
        prev += 1
    utils.p(inc)

if __name__ == "__main__":
    main()

