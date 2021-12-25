import re
import heapq
from functools import *

# https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
# Find multiplicative inverse of a mod b
def mul_inv(a,b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1

# https://rosettacode.org/wiki/Chinese_remainder_theorem
# n, a lists of ints, same length
# n the list of modulo bases
# a the list of remainders (modulo congruences)
# ex: x = 2 (mod 3) = 3 (mod 5) = 2 (mod 7)
# n = [3, 5, 7]
# a = [2, 3, 2]
# answer is 23 (23 % 3 = 2, 23 % 5 = 3, 23 % 7 = 2)
def crt(n, a):
    N = reduce(lambda x, y: x*y, n)
    x = 0
    for i in range(len(n)):
        ni = n[i]
        ai = a[i]
        pi = N//ni
        si = mul_inv(pi, ni)
        x += ai * si * pi
    x = x % N
    return x

# shorthand for print
def p(arg):
    print(arg)

# read input into string
def getinput():
    with open('input.txt', 'r') as f:
        return f.read()

# split input into 2d list, one inner list per \n\n 
def getdbnldata():
    data = getinput()
    groups = data.split('\n\n')
    for i in range(len(groups)):
        groups[i] = list(filter(lambda x: x != '', groups[i].split('\n')))
    return groups

# split inputs into lines
def getlines():
    return getinput().splitlines()

# map func onto input lines
def getlines_map(func):
    return list(map(func, getlines()))

# get input as list of ints
def getlines_int():
    return getlines_map(int)

# get input as lines, stripped of whitespace
def getlines_strip():
    return getlines_map(lambda x: x.strip())

# get input as lines, split by delimiter
def getlines_getsv(delim=','):
    return getlines_map(lambda x: x.split(delim))

# get input as ints, split by delimiter
def getlines_getsv_int(delim=','):
    return list(map(lambda x: list(map(int, x)), getlines_getsv(delim)))

# get input as lines mapped with regex pattern
def getlines_map_regex(pattern_string):
    return getlines_map(lambda x: re.fullmatch(re.compile(pattern_string), x))

# run filter on input lines
def getlines_filter(func):
    lines = getlines()
    return list(filter(func, lines))

# run regex filter on input lines
def getlines_filter_regex(pattern_string):
    return getlines_filter(lambda x: bool(re.fullmatch(re.compile(pattern_string), x)))

class Node:
    def __init__(self, label):
        self.edges = []
        self.label = label

    def get_label(self):
        return self.label

    def add_edge(self, weight, node):
        self.edges.append((weight, node))

    def get_edges(self):
        return self.edges

class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, name):
        node = Node(name)
        self.graph[name] = node

    def __contains__(self, key):
        return (key in self.graph)

    def get_node(self, name):
        return self.graph[name]

    def add_edge(self, from_name, to_name, weight):
        from_node = self.get_node(from_name)
        to_node = self.get_node(to_name)
        from_node.add_edge(weight, to_node)

    def dijkstra(self, source, target=None):
        Q = set()
        dist = {}
        prev = {}
        for v in self.graph:
            dist[v] = 999999999999
            prev[v] = None
            Q.add(v)
        dist[source] = 0

        Qheap = [(0, source)]
        while len(Qheap) > 0:
            esti, u = heapq.heappop(Qheap)
            if u in Q:
                Q.remove(u)
            if esti > dist[u]:
                continue

            if target is not None and u == target:
                break

            edges = self.get_node(u).get_edges()
            for edge in edges:
                length = edge[0]
                v = edge[1].get_label()
                if v not in Q:
                    continue
                alt = esti + length
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
                    heapq.heappush(Qheap, (alt, v))
        
        return dist, prev

