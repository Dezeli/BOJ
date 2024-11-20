# 배열 정렬
import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
A = [0] + list(map(int, input().split()))
M = int(input())
swap = [list(map(int, input().split())) for _ in range(M)]

need = sorted(A)

visit = defaultdict(int)
heap = []
heapq.heappush(heap, (0, A))

find = False
while heap:
    cost, li = heapq.heappop(heap)
    if li==need:
        find = True
        break

    if visit[tuple(li)]:
        continue
    visit[tuple(li)] = 1

    for l, r, c in swap:
        new_li = li.copy()
        new_c = cost + c
        new_li[l], new_li[r] = new_li[r], new_li[l]
        heapq.heappush(heap, (new_c, new_li))

if find:
    print(cost)
else:
    print(-1)