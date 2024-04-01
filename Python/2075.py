# N번째 큰 수
import sys
import heapq

input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    nums = map(int, input().split())
    for n in nums:
        if len(heap) < N:
            heapq.heappush(heap, n)
        else:
            if heap[0] < n:
                heapq.heappop(heap)
                heapq.heappush(heap, n)
print(heap[0])