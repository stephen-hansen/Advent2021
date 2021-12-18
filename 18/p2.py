import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from collections import defaultdict, Counter
from functools import reduce
from utils import *
import copy
import ast

class myNode:
    def __init__(self):
        self.parent = None
        self.left = None
        self.right = None
        self.value = None
    def set_parent(self, p):
        self.parent = p
    def set_left(self, l):
        self.left = l
    def set_right(self, r):
        self.right = r
    def set_conn(self, c):
        if self.left is None:
            self.left = c
        else:
            self.right = c
    def set_value(self, v):
        self.value = v

def get_leftmost_pair(n, d=0):
    if n is None:
        return None
    if d == 4:
        if n.value is None:
            return n
        else:
            return None
    cand = get_leftmost_pair(n.left, d+1)
    if cand is not None:
        return cand
    return get_leftmost_pair(n.right, d+1)

def get_leftmost_number(n):
    if n is None:
        return None
    if n.value is not None:
        if n.value >= 10:
            return n
        else:
            return None
    cand = get_leftmost_number(n.left)
    if cand is not None:
        return cand
    return get_leftmost_number(n.right)

def explode(pairNode):
    lvalue = pairNode.left.value
    rvalue = pairNode.right.value
    pairNode.set_left(None)
    pairNode.set_right(None)
    pairNode.set_value(0)
    parent_node = pairNode.parent
    prev_parent = pairNode
    while parent_node is not None:
        if parent_node.left is not None and parent_node.left is not prev_parent:
            break
        prev_parent = parent_node
        parent_node = parent_node.parent
    if parent_node is not None:
        leftmost_node = parent_node.left
        while leftmost_node.right is not None:
            leftmost_node = leftmost_node.right
        # Got leftmost node, update value
        leftmost_node.value = leftmost_node.value + lvalue
    parent_node = pairNode.parent
    prev_parent = pairNode
    while parent_node is not None:
        if parent_node.right is not None and parent_node.right is not prev_parent:
            break
        prev_parent = parent_node
        parent_node = parent_node.parent
    if parent_node is not None:
        rightmost_node = parent_node.right
        while rightmost_node.left is not None:
            rightmost_node = rightmost_node.left
        # Got rightmost node, update value
        rightmost_node.value = rightmost_node.value + rvalue

def split(valueNode):
    regnumber = valueNode.value
    valueNode.value = None
    leftnode = myNode()
    leftnode.parent = valueNode
    leftnode.value = regnumber // 2
    rightnode = myNode()
    rightnode.parent = valueNode
    rightnode.value = regnumber // 2 + (regnumber % 2)
    valueNode.left = leftnode
    valueNode.right = rightnode

def reduce_number(snailfish):
    while True:
        inorder(snailfish)
        #p('')
        can_break = True
        # Get leftmost pair at d=4
        cand = get_leftmost_pair(snailfish)
        if cand is not None:
            # Explode it
            #p("Explode")
            explode(cand)
            can_break = False
        else:
            # Get leftmost regular number 10 or greater
            cand = get_leftmost_number(snailfish)
            if cand is not None:
                # Split it
                #p("Split")
                split(cand)
                can_break = False
        if can_break:
            break

def add(snail1, snail2):
    root = myNode()
    root.left = snail1
    snail1.parent = root
    root.right = snail2
    snail2.parent = root
    reduce_number(root)
    return root

def inorder(root):
    return
    if root.value is not None:
        print(root.value, end='')
    else:
        print('[', end='')
        inorder(root.left)
        print(',', end='')
        inorder(root.right)
        print(']', end='')

def magnitude(root):
    if root.value is not None:
        return root.value
    else:
        return 3*magnitude(root.left) + 2*magnitude(root.right)

def line_to_tree(l):
    curr = None
    for c in l:
        if c == '[':
            new = myNode()
            new.set_parent(curr)
            if curr is not None:
                curr.set_conn(new)
            curr = new
        elif c == ']':
            if curr.parent is not None:
                curr = curr.parent
        elif c == ',':
            continue
        else:
            v = int(c)
            new = myNode()
            new.set_value(v)
            new.set_parent(curr)
            if curr is not None:
                curr.set_conn(new)
    return curr

def main():
    A = getlines()
    largest_magnitude = -1
    for i in range(len(A)):
        for j in range(len(A)):
            if i == j:
                continue
            t1 = line_to_tree(A[i])
            t2 = line_to_tree(A[j])
            t3 = add(t1, t2)
            m = magnitude(t3)
            if m > largest_magnitude:
                largest_magnitude = m
    p(largest_magnitude)

if __name__ == "__main__":
    main()

