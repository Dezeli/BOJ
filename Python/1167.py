# 트리의 지름
import sys
from collections import defaultdict, deque

input = sys.stdin.readline

V = int(input())
Tree = defaultdict(list)
simple_Tree = defaultdict(list)

for _ in range(V):
    lines = list(map(int, input().split()))
    for i in range(1, len(lines)-1, 2):
        Tree[lines[0]].append([lines[i], lines[i+1]])

nodes = deque([1])
while nodes:
    n = nodes.popleft()
    for e, l in Tree[n]:
        if simple_Tree[e]:
            continue
        simple_Tree[n].append([e, l])
        nodes.append(e)


max_line = []

def search(n):
    line_lens = [0, 0]
    for line in simple_Tree[n]:
        next, l = line
        down = search(next)
        line_lens.append(down+l)
    
    line_lens.sort(reverse=True)
    max_line.append(line_lens[0] + line_lens[1])
    return line_lens[0]

search(1)
print(max(max_line))