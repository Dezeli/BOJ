# 다리 놓기
import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    cnt = 1
    for n in range(N):
        cnt *= M - n
        cnt /= n + 1
    print(int(cnt))
