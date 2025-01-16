# 중량제한
import sys, heapq
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())

bridge = defaultdict(list)

for _ in range(M):
    A, B, C = map(int, input().split())
    bridge[A].append([C, B])
    bridge[B].append([C, A])

start, end = map(int, input().split())

root = [[-10**9, start]]
max_w = [0 for i in range(N+1)]
while root:
    w, n = heapq.heappop(root)
    if max_w[n] >= -w:
        continue
    max_w[n] = -w
    if n==end:
        continue

    for w1, n1 in bridge[n]:
        heapq.heappush(root, [-min(w1, -w), n1])

print(max_w[end])