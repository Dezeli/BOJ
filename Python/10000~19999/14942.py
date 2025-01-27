# 개미
import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())

ants = [0] + [int(input()) for _ in range(n)]
arrive = [1 for _ in range(n + 1)]
visit = [0 for _ in range(n + 1)]
road = defaultdict(list)


for i in range(n - 1):
    a, b, c = map(int, input().split())
    road[a].append([b, c])
    road[b].append([a, c])


def move(r, d):
    nums = [r]
    visit[r] = 1
    for b, c in road[r]:
        if visit[b]:
            continue
        nums += move(b, c)

    lnums = []
    for i in nums:
        ants[i] -= d
        if ants[i] < 0:
            arrive[i] = r
        else:
            lnums.append(i)
    return lnums


move(1, 0)

for i in arrive[1:]:
    print(i)
