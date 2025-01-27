# 카드1
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

cards = deque([i for i in range(1, N + 1)])


order = []
cnt = 0
while cards:
    if cnt % 2 == 0:
        order.append(cards.popleft())
    else:
        cards.append(cards.popleft())
    cnt += 1

print(*order)
