import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import *

def main():
    data = getlines_map_regex('(.*) (.*)')
    horiz = 0
    depth = 0
    fake_depth = 0
    for item in data:
        direct = item.group(1)
        amt = int(item.group(2))
        if direct == 'forward':
            horiz += amt
            fake_depth += depth * amt
        elif direct == 'down':
            depth += amt
        elif direct == 'up':
            depth -= amt
    p(fake_depth*horiz)

if __name__ == "__main__":
    main()

