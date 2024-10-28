# 돌 게임 4
import sys

input = sys.stdin.readline

N = int(input())

dp = [0] * 1001
dp[1], dp[2], dp[3], dp[4] = 0, 1, 0, 1

for i in range(5, N + 1):
    if dp[i - 1] and dp[i - 3] and dp[i - 4]:
        dp[i] = 0
    else:
        dp[i] = 1

if dp[N] == 1:
    print("SK")
else:
    print("CY")
