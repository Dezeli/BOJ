# 공
import sys

T = int(sys.stdin.readline().rstrip())
ball = 1
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    if N == ball:
        ball = M
    elif M == ball:
        ball = N
print(ball)
