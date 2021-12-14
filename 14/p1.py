import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from collections import defaultdict, Counter
from functools import reduce
from utils import *
import copy

def main():
    A = getlines()
    template = A[0]
    steps = { y[0]: y[1] for y in list(map(lambda x: x.split(" -> "), A[2:])) }
    for k in range(10):
        new = template[0]
        for i in range(len(template)-1):
            combo = template[i:i+2]
            if combo in steps:
                new += steps[combo]
            new += combo[-1]
        template = new
    counts = Counter(template).most_common()
    most_common = counts[0]
    least_common = counts[-1]
    p(most_common[1] - least_common[1])

if __name__ == "__main__":
    main()

