# 과자
import sys

K, N, M = map(int, sys.stdin.readline().split())
if K * N <= M:
    print(0)
else:
    print(K * N - M)
