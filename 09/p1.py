import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from collections import defaultdict
from functools import reduce
from utils import *
import copy

def main():
    A = getlines_map_regex("(.*) \| (.*)")
    c = 0
    p(c)

if __name__ == "__main__":
    main()

