# 정점들의 거리
import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())

graph = defaultdict(list)

for _ in range(N-1):
    n1, n2, d = map(int, input().split())
    graph[n1].append([n2, d])
    graph[n2].append([n1, d])

node_depth = [-1 for i in range(N+1)]
node_distance = [-1 for i in range(N+1)]

queue = [1]
node_depth[1] = 0
node_distance[1] = 0
parent = [[0]*16 for _ in range(N+1)]

while queue:
    n1 = queue.pop()
    for n2, d in graph[n1]:
        if node_depth[n2]==-1:
            node_depth[n2] = node_depth[n1] + 1
            node_distance[n2] = node_distance[n1] + d
            parent[n2][0] = n1
            queue.append(n2)

for k in range(1, 16):
    for n in range(1, N + 1):
        parent[n][k] = parent[parent[n][k-1]][k-1]


def LCA(n1, n2):
    if node_depth[n1] < node_depth[n2]:
        n1, n2 = n2, n1
    
    diff = node_depth[n1]-node_depth[n2]
    for k in range(16):
        if (diff >> k) & 1:
            n1 = parent[n1][k]

    if n1==n2:
        return n1
    else:
        for k in range(16):
            if parent[n1][15-k] != parent[n2][15-k]:
                n1 = parent[n1][15-k]
                n2 = parent[n2][15-k]
        return parent[n1][0]


M = int(input())
for _ in range(M):
    n1, n2 = map(int, input().split())
    lca_node = LCA(n1, n2)

    print(node_distance[n1]+node_distance[n2]-2*node_distance[lca_node])