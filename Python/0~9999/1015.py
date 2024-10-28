# 수열 정렬
import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().split()))
P = [-1 for _ in range(N)]

sorted_A = sorted(A)

num = 0
for i in sorted_A:
    idx = A.index(i)
    P[idx] = num
    A[idx] = -1
    num += 1

for i in range(len(P) - 1):
    print(P[i], end=" ")
print(P[-1])
