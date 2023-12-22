# 특정한 최단 경로
import sys
from collections import defaultdict

input = sys.stdin.readline

N, E = map(int, input().split(" "))

Graph = defaultdict(list)

for _ in range(E):
    u, v, d = map(int, input().split(" "))
    Graph[u].append([v, d])
    Graph[v].append([u, d])

v1, v2 = map(int, input().split(" "))
print(Graph)


def short_move(start, final):
    short_distance = [sys.maxsize for _ in range(N+1)]
    short_distance[start] = 0

    moves = []
    for v, d in Graph[start]:
        moves.append([v, d])

    while moves:
        v, d = moves.pop()
        if v==final:
            short_distance[final] = min([short_distance[final], d])
            continue
        else:
            if short_distance[final]<=d:
                continue
            else:
                short_distance[final] = d
                for newv, newd in Graph[start]:
                    moves.append([newv, newd+d])
    print(short_distance)
    return short_distance[final]


print(short_move(1, 4))
