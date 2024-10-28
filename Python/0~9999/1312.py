# 소수
import sys

A, B, N = map(int, sys.stdin.readline().split())

A = A % B
cnt = 0

while cnt < N:
    cnt += 1
    A *= 10
    result = A // B
    A = A % B
print(result)
