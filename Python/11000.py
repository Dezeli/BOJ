# 강의실 배정
import sys
import heapq

input = sys.stdin.readline

N = int(input())

times = []

for _ in range(N):
    times.append(list(map(int, input().split())))
times.sort()

heap = [times[0][1]]
for i in range(1, N):
    if heap[0] <= times[i][0]:
        heapq.heappop(heap)
    heapq.heappush(heap,times[i][1])

print(len(heap))