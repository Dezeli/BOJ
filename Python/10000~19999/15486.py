# 퇴사 2
import sys

input = sys.stdin.readline

N = int(input())
conseling = [[0, 0]] + [map(int, input().split()) for _ in range(N)]

dp = [0 for i in range(N + 1)]

for i in range(1, N + 1):
    T, P = conseling[i]
    if dp[i] < dp[i - 1]:
        dp[i] = dp[i - 1]
    if i + T - 1 <= N:
        dp[i + T - 1] = max(dp[i + T - 1], dp[i - 1] + P)
print(max(dp))
