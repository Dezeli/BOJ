# LCA 2
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

max_len = 21

N = int(input())
parent = [[0] * max_len for _ in range(N + 1)]
visit = [False] * (N + 1)
d = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(x, depth):
    visit[x] = True
    d[x] = depth

    for n in graph[x]:
        if visit[n]:
            continue

        parent[n][0] = x
        dfs(n, depth + 1)


def set_parent():
    dfs(1, 0)
    for i in range(1, max_len):
        for j in range(1, N + 1):
            parent[j][i] = parent[parent[j][i - 1]][i - 1]


def lca(a, b):
    if d[a] > d[b]:
        a, b = b, a

    for i in range(max_len - 1, -1, -1):
        if d[b] - d[a] >= 2**i:
            b = parent[b][i]

    if a == b:
        return a

    for i in range(max_len - 1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]

    return parent[a][0]


set_parent()

M = int(input())

for _ in range(M):
    a, b = map(int, input().split())
    print(lca(a, b))
