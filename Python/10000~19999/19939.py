# 박 터뜨리기
import sys

input = sys.stdin.readline

N, K = map(int, input().split())

start = [i for i in range(1, K + 1)]

if sum(start) > N:
    print(-1)
else:
    N -= sum(start)
    dif = K - 1
    if N % K > 0:
        dif += 1
    print(dif)
