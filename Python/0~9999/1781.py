# 컵라면
import sys
import heapq

input = sys.stdin.readline

N = int(input())

quiz = []

for _ in range(N):
    d, r = map(int, input().split())
    quiz.append((d, r))

quiz.sort()

ramen_heap = []

for d, r in quiz:
    heapq.heappush(ramen_heap, r)
    
    if len(ramen_heap) > d:
        heapq.heappop(ramen_heap)

print(sum(ramen_heap))