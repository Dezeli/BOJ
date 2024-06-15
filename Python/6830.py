# It's Cold Here!
import heapq

heap = []

c, t = input().split()
heapq.heappush(heap, [int(t), c])

while c!="Waterloo":
    c, t = input().split()
    heapq.heappush(heap, [int(t), c])

print(heapq.heappop(heap)[1])