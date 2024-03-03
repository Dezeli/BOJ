# 분산처리
import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    a = int(str(a)[-1])
    b = b % 4
    if b == 0:
        b = 4
    if a**b % 10 == 0:
        print(10)
    else:
        print(a**b % 10)
