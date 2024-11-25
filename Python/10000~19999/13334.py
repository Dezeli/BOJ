# 철로
import sys
import heapq

input = sys.stdin.readline

sQ = []
bQ = []

n = int(input())
lines = [list(map(int, input().split())) for _ in range(n)]

d = int(input())

for h, o in lines:
    if abs(h-o) > d:
        continue
    heapq.heappush(sQ, min(h, o))
    heapq.heappush(bQ, max(h, o))


max_p = 0
cur_p = 0
while bQ:
    b = heapq.heappop(bQ)
    cur_p += 1
    while sQ:
        s = heapq.heappop(sQ)
        if s >= b-d:
            heapq.heappush(sQ, s)
            break
        cur_p -= 1
    max_p = max(max_p, cur_p)

print(max_p)
