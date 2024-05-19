# 보석 도둑
import sys
import heapq

input = sys.stdin.readline
N, K = map(int, input().split())

jewerly = []
for _ in range(N):
    heapq.heappush(jewerly, list(map(int, input().split())))

bags = [int(input()) for _ in range(K)]
bags.sort()


sum_val = 0
fit = []
for C in bags:
    while jewerly and C>=jewerly[0][0]:
        heapq.heappush(fit, -heapq.heappop(jewerly)[1])
    if fit:
        sum_val -= heapq.heappop(fit)
    elif not jewerly:
        break

print(sum_val)
