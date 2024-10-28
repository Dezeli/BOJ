# 최대 힙
import sys
import heapq

N = int(sys.stdin.readline().rstrip())
heap = []

for _ in range(N):
    order = int(sys.stdin.readline().rstrip())
    if order == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (-order, order))
