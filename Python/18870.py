# 좌표 압축
import sys
import heapq
import collections

N = int(sys.stdin.readline().rstrip())
Xs = list(map(int, sys.stdin.readline().split()))
setX = list(set(Xs))
heap = []
for i in setX:
    heapq.heappush(heap, i)

order = collections.defaultdict(int)
for i in range(len(heap)):
    order[heapq.heappop(heap)] = i

for x in Xs:
    print(order[x], end=" ")