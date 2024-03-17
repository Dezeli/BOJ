# 수들의 합 2
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

A = list(map(int, input().split())) + [0]

l, r = 0, 0
sum_num = A[0]
cnt = 0

while True:
    if r == N:
        break

    if sum_num == M:
        cnt += 1
        r += 1
        sum_num += A[r]
    elif sum_num > M:
        sum_num -= A[l]
        l += 1
    else:
        r += 1
        sum_num += A[r]

print(cnt)