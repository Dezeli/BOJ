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

max_t = [-1 for _ in range(n+1)]

move = [[s, 0]]

while move:
    b, t = move.pop()
    if max_t[b]>=t:
        continue
    max_t[b] = t

    for b1, t1 in roads[b]:
        move.append([b1, t+t1])

visit = defaultdict(int)

max_time = []



print(max_t[e])
