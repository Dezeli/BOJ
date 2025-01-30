# LCA 2
import sys
from collections import defaultdict

input = sys.stdin.readline

graph = defaultdict(list)

N = int(input())
for i in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0 for _ in range(N+1)]

def search(n, d, p):
    if parent[n]!=0:
        return
    parent[n] = {(d, n)}|p

    for i in graph[n]:
        search(i, d+1, parent[n])

search(1, 0, set())


M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(max(parent[a]&parent[b])[1])
