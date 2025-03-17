# 공주님의 정원
import sys
import heapq

input = sys.stdin.readline
convert = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]


N = int(input())
dates = []
for _ in range(N):
    a1, a2, b1, b2 = map(int, input().split())
    dates.append([convert[a1-1]+a2, convert[b1-1]+b2])
dates.sort()

last = 60
heap = []
heapq.heappush(heap, 1)
cnt = 0
pos = True
for s, e in dates:
    if s>last:
        cnt += 1
        last = -heapq.heappop(heap)
        heap = []
        if last>334:
            break
        if s>last:
            pos = False
            break
        heapq.heappush(heap, -e)
    else:
        heapq.heappush(heap, -e)

if heap:
    cnt += 1
    last = -heapq.heappop(heap)
    if last<=334:
        pos = False

if pos:
    print(cnt)
else:
    print(0)