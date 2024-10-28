# 케빈 베이컨의 6단계 법칙
import sys
from collections import defaultdict, deque

N, M = map(int, sys.stdin.readline().split(" "))
graph = defaultdict(list)

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split(" "))
    graph[A].append(B)
    graph[B].append(A)


def BFS(N, graph, root):
    visited = []
    queue = deque([root])
    KB = [0 for _ in range(N)]

    while queue:
        n, row = queue.popleft()
        if n not in visited:
            visited.append(n)
            KB[n - 1] = row
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort()
                for p in temp:
                    queue.append([p, row + 1])
    return sum(KB)


KBs = [sys.maxsize]

for i in range(1, N + 1):
    KBs.append(BFS(N, graph, [i, 0]))

print(KBs.index(min(KBs)))
