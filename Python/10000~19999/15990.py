# 1, 2, 3 더하기 5
import sys

input = sys.stdin.readline

dp = [[0 for _ in range(3)] for _ in range(100001)]

dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]

mod = 1000000009

for i in range(4, 100001):
    dp[i][0] = (dp[i - 1][1] + dp[i - 1][2]) % mod
    dp[i][1] = (dp[i - 2][0] + dp[i - 2][2]) % mod
    dp[i][2] = (dp[i - 3][0] + dp[i - 3][1]) % mod

T = int(input())
for i in range(T):
    n = int(input())
    print(sum(dp[n]) % mod)
