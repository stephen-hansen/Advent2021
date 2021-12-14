import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from collections import defaultdict, Counter
from functools import reduce
from utils import *
import copy

MEMO = {}

def memoized(pair, steps, j, limit):
    key = (pair, j)
    if key in MEMO:
        return copy.deepcopy(MEMO[key])
    if j == limit:
        return defaultdict(int)
    c = steps[pair]
    counts = memoized(pair[0] + c, steps, j+1, limit)
    counts[c] += 1
    d2 = memoized(c + pair[1], steps, j+1, limit)
    for k, v in d2.items():
        counts[k] += v
    MEMO[key] = counts
    return copy.deepcopy(MEMO[key])

def main():
    A = getlines()
    template = A[0]
    steps = { y[0]: y[1] for y in list(map(lambda x: x.split(" -> "), A[2:])) }
    pairs = []
    for i in range(len(template)-1):
        pairs.append(template[i:i+2])
    counts = defaultdict(int)
    for c in template:
        counts[c] += 1
    for pair in pairs:
        new_counts = memoized(pair, steps, 0, 40)
        for k, v in new_counts.items():
            counts[k] += v
    most_common = max(counts.values())
    least_common = min(counts.values())
    p(most_common - least_common)

if __name__ == "__main__":
    main()

