# 국회의원 선거
import sys
import heapq

input = sys.stdin.readline

N = int(input())

dasom = int(input())

cnt = 0
heap = []

for _ in range(N-1):
    heapq.heappush(heap, -int(input()))


while heap:
    a = -heapq.heappop(heap)

    if dasom>a:
        break

    cnt += 1
    dasom += 1
    heapq.heappush(heap, -a+1)

print(cnt)
