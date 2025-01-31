# 이분 그래프
import sys
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

K = int(input())

def search(n, c):
    global bipartite
    if visit[n]:
        if c!=color[n]:
            bipartite = False
        return
    
    visit[n] = True
    color[n] = c

    for i in graph[n]:
        search(i, not c)



for _ in range(K):
    V, E = map(int, input().split())

    graph = defaultdict(list)
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    bipartite = True
    color = [True for _ in range(V+1)]
    visit = [False for _ in range(V+1)]
    for i in range(V):
        if not visit[i]:
            search(i, True)
            
    if bipartite:
        print("YES")
    else:
        print("NO")