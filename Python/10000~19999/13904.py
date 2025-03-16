# 과제
import sys
import heapq

input = sys.stdin.readline

N = int(input())

heap = []
max_day = 0
for _ in range(N):
    d, w = map(int, input().split())
    max_day = max(max_day, d)
    heapq.heappush(heap, [-w, d])

score = 0
new = []
while heap:
    if max_day==0:
        break
    w, d = heapq.heappop(heap)
    if d < max_day:
        new.append([w, d])
        if heap:
            continue
        max_day -= 1
        while new:
            w1, d1 = new.pop()
            heapq.heappush(heap, [w1, d1])
    else:
        score -= w
        max_day -= 1
        while new:
            w1, d1 = new.pop()
            heapq.heappush(heap, [w1, d1])
    

print(score)
