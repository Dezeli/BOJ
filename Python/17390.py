# 이건 꼭 풀어야 해!
import sys

input = sys.stdin.readline

N, Q = map(int, input().split())
A = sorted(list(map(int, input().split())))

sum_A = [0]
for i in A:
    sum_A.append(sum_A[-1] + i)

for _ in range(Q):
    L, R = map(int, input().split())

    print(sum_A[R] - sum_A[L - 1])
