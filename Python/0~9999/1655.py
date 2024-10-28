# 가운데를 말해요
import sys
import heapq

input = sys.stdin.readline

N = int(input())

lheap = []
rheap = []
for i in range(N):
    num = int(input())

    if len(lheap) == len(rheap):
        heapq.heappush(lheap, -num)
    else:
        heapq.heappush(rheap, num)

    if rheap and rheap[0] < -lheap[0]:
        leftValue = heapq.heappop(lheap)
        rightValue = heapq.heappop(rheap)

        heapq.heappush(lheap, -rightValue)
        heapq.heappush(rheap, -leftValue)

    print(-lheap[0])
