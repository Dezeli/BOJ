# 트리 순회
import sys
from collections import defaultdict

N = int(sys.stdin.readline().rstrip())

relation = defaultdict(list)

for _ in range(N):
    p, cl, cr = list(sys.stdin.readline().rstrip().split(" "))
    relation[p] = [cl, cr]


DLR_result = []
LDR_result = []
LRD_result = []

def DLR(node):
    if node == '.':
        return
    
    DLR_result.append(node)
    DLR(relation[node][0])
    DLR(relation[node][1])


def LDR(node):
    if node == '.':
        return
    
    LDR(relation[node][0])
    LDR_result.append(node)
    LDR(relation[node][1])

def LRD(node):
    if node == '.':
        return
    
    LRD(relation[node][0])
    LRD(relation[node][1])
    LRD_result.append(node)

DLR('A')
print(''.join(DLR_result))
LDR('A')
print(''.join(LDR_result))
LRD('A')
print(''.join(LRD_result))