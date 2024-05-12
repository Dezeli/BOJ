# 가장 큰 증가하는 부분 수열
import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

d = [1] * N
d[0] = A[0]
for i in range(1, N):
    for j in range(i):
        if A[j] < A[i]:
            d[i] = max(d[i], d[j] + A[i])
        else:
            d[i] = max(d[i], A[i])

print(max(d))
