# 카드 정렬하기
import sys
import heapq

input = sys.stdin.readline

N = int(input())

heap = []

for _ in range(N):
    heapq.heappush(heap, int(input()))

check = 0

while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    check += a + b
    heapq.heappush(heap, a + b)

print(check)
