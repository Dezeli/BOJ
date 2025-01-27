# 임계경로
import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
m = int(input())

roads = defaultdict(list)
reverse_road = defaultdict(list)

for _ in range(m):
    a, b, t = map(int, input().split())
    roads[a].append([b, t])
    reverse_road[b].append([a, t])

s, e = map(int, input().split())

max_t = [-1 for _ in range(n + 1)]

move = [[s, 0]]

while move:
    b, t = move.pop()
    if max_t[b] >= t:
        continue
    max_t[b] = t

    for b1, t1 in roads[b]:
        move.append([b1, t + t1])

visit = defaultdict(int)

road_cnt = 0
move = [[e, max_t[e]]]
while move:
    a, t = move.pop()

    for a1, t1 in reverse_road[a]:
        if visit[(a, a1)] == 1:
            continue
        if max_t[a1] != t - t1:
            continue
        road_cnt += 1
        visit[(a, a1)] = 1
        move.append([a1, t - t1])

print(max_t[e])
print(road_cnt)
