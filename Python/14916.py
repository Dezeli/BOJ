# 거스름돈
import sys

input = sys.stdin.readline

n = int(input())
INF = 10**5
dp = [INF for _ in range(100001)]
dp[2] = 1
dp[4] = 2
dp[5] = 1

for i in range(6, n+1):
    if dp[i-2]!=INF:
        dp[i] = min(dp[i], dp[i-2]+1)
    if dp[i-5]!=INF:
        dp[i] = min(dp[i], dp[i-5]+1)

if dp[n]<INF:
    print(dp[n])
else:
    print(-1)
