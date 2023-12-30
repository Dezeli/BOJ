# 트리의 지름
import sys
from collections import defaultdict 

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())

root = 1
Tree = defaultdict(list)

for _ in range(n-1):
    u, v, d = map(int, input().split(" "))
    Tree[u].append([v, d])



lens = [0]
def longest(pNode, d):
    if not Tree[pNode]:
        return d

    childs = [longest(cNode, d) for cNode, d in Tree[pNode]]
    childs.sort(reverse=True)
    if len(childs)>1:
        lens.append(childs[0]+childs[1])
    else:
        lens.append(childs[0])
    return d + childs[0]
        
longest(root, 0)
print(max(lens))
