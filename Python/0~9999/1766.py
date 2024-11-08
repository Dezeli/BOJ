# 문제집
import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())


can_solve = [0 for _ in range(N + 1)]
hint_dict = defaultdict(list)

for _ in range(M):
    A, B = map(int, input().split())
    can_solve[B] += 1
    hint_dict[A].append(B)

heap = []
for i in range(1, N + 1):
    if can_solve[i] == 0:
        heapq.heappush(heap, i)

order = []
while heap:
    i = heapq.heappop(heap)
    order.append(i)
    for j in hint_dict[i]:
        can_solve[j] -= 1
        if can_solve[j] == 0:
            heapq.heappush(heap, j)

print(*order)
