# 외판원 순회 3
import sys

input = sys.stdin.readline

N = int(input())

location = [list(map(int, input().split())) for _ in range(N)]
move = []
for x1, y1 in location:
    city = []
    for x2, y2 in location:
        city.append(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2))
    move.append(city)

data = {}


def DFS(cur, visited):
    if visited == (1 << N) - 1:
        if move[cur][0]:
            return move[cur][0]
        else:
            return int(1e9)

    if (cur, visited) in data:
        return data[(cur, visited)]

    min_cost = int(1e9)
    for next in range(1, N):
        if move[cur][next] == 0 or visited & (1 << next):
            continue
        cost = DFS(next, visited | (1 << next)) + move[cur][next]
        min_cost = min(cost, min_cost)

    data[(cur, visited)] = min_cost
    return min_cost


print(DFS(0, 1))
