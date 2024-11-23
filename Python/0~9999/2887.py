# 행성 터널
from collections import defaultdict
import sys


input = sys.stdin.readline

N = int(input())

planet = [[] for _ in range(3)]
for i in range(N):
    loc = tuple(map(int, input().split()))
    for j in range(3):
        planet[j].append((loc[j], i))

tunels = defaultdict(lambda: 10**9)

for j in range(3):
    planet[j].sort()
    for i in range(N - 1):
        p1, i1 = planet[j][i]
        p2, i2 = planet[j][i + 1]
        tunels[(i1, i2)] = min(abs(p1 - p2), tunels[(i1, i2)])

tunels = list(tunels.items())
tunels.sort(key=lambda x: -x[1])

parent = [i for i in range(N)]


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    parent[max(x, y)] = min(x, y)


cnt, d = 0, 0
while cnt < N - 1:
    p, cost = tunels.pop()
    a, b = p
    pa, pb = find(a), find(b)
    if pa != pb:
        union(pa, pb)
        d += cost
        cnt += 1

print(d)
