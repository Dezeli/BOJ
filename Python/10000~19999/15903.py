# 카드 합체 놀이
import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())

cards = []
for i in map(int, input().split()):
    heapq.heappush(cards, i)

for _ in range(m):
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    heapq.heappush(cards, a+b)
    heapq.heappush(cards, a+b)

print(sum(cards))