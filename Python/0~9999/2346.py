# 풍선 터뜨리기
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

papers = [0] + list(map(int, input().split()))
ballons = deque([i for i in range(1, N+1)])

order = []

for _ in range(N-1):
    a = ballons.popleft()
    order.append(a)
    move = papers[a]
    if move>0:
        for __ in range(move-1):
            ballons.append(ballons.popleft())
    else:
        for __ in range(-move):
            ballons.appendleft(ballons.pop())
order.append(ballons.pop())

print(*order)