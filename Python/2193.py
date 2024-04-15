# 이친수
import sys

input = sys.stdin.readline

N = int(input())

zero = [0 for _ in range(N)]
one = [0 for _ in range(N)]
one[0] = 1

for i in range(1, N):
    zero[i] = zero[i-1] + one[i-1]
    one[i] = zero[i-1]

print(zero[N-1] + one[N-1])