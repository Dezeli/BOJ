# 블록 놀이
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

minimum = N
for i in range(N):
    cnt = 1
    num = A[i]
    minus = False
    for j in range(i):
        if num - (K * (i - j)) < 1:
            minus = True
            break
        if A[j] == num - (K * (i - j)):
            cnt += 1
    for j in range(i + 1, N):
        if num + (K * (j - i)) < 1:
            minus = True
            break
        if A[j] == num + (K * (j - i)):
            cnt += 1
    if not minus:
        minimum = min(N - cnt, minimum)

print(minimum)
