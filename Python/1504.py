# 특정한 최단 경로
import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N, E = map(int, input().split(" "))

Graph = defaultdict(list)

for _ in range(E):
    u, v, d = map(int, input().split(" "))
    Graph[u].append([v, d])
    Graph[v].append([u, d])

v1, v2 = map(int, input().split(" "))


def short_move(start, final):
    short_distance = [sys.maxsize for _ in range(N+1)]
    short_distance[start] = 0

    moves = deque(Graph[start])

    while moves:
        v, d = moves.popleft()
        if v==final:
            short_distance[final] = min([short_distance[final], d])
            continue
        else:
            if short_distance[v]<=d:
                continue
            else:
                short_distance[v] = d
                for newv, newd in Graph[start]:
                    moves.append([newv, newd+d])
    return short_distance[final]


route1 = short_move(1, v1)+ short_move(v1, v2) + short_move(v2, N)
route2 = short_move(1, v2)+ short_move(v2, v1) + short_move(v1, N)
print(min([route1, route2]))