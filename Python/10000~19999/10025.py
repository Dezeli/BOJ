# 게으른 백곰
import sys
from collections import defaultdict

input = sys.stdin.readline

N, K = map(int, input().split())

ice = defaultdict(int)

search = 0
for _ in range(N):
    g, x = map(int, input().split())
    ice[x] = g

l = 0
r = K * 2

cur_sum = 0
for i in range(r + 1):
    cur_sum += ice[i]
max_sum = cur_sum

while r <= 1000000:
    cur_sum -= ice[l]
    l += 1
    r += 1
    cur_sum += ice[r]

    max_sum = max(max_sum, cur_sum)
print(max_sum)
