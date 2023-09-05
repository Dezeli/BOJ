# 책 정리
import sys

N, M = map(int, sys.stdin.readline().split())

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
space = 0

for b in B:
    while True:
        if A[0] - b >= 0:
            A[0] -= b
            break
        else:
            space += A.pop(0)
for a in A:
    space += a

print(space)
