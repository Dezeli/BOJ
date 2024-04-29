# 돌 게임 2
import sys

input = sys.stdin.readline

N = int(input())

dp = [0 for _ in range(1001)]
dp[2] = 1
dp[4] = 1

for i in range(5, N+1):
    if dp[i-1]==0 or dp[i-3]==0:
        dp[i] = 1

if dp[N]==0:
    print("CY")
else:
    print("SK")