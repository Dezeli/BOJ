# 절댓값 힙
import sys
import heapq

N = int(sys.stdin.readline().rstrip())
heap = []

for _ in range(N):
    x = int(sys.stdin.readline().rstrip())

    if x == 0:
        if heap:
            num, sign = heapq.heappop(heap)
            print(num * sign)
        else:
            print(0)
    else:
        if x < 0:
            heapq.heappush(heap, [-x, -1])
        else:
            heapq.heappush(heap, [x, 1])
