# BABBA 
import sys

input = sys.stdin.readline

K = int(input())
dp = [[0, 0] for _ in range(K+1)]
dp[0][0] = 1

for i in range(1, K+1):
    dp[i][0] = dp[i-1][1]
    dp[i][1] = dp[i-1][0] + dp[i-1][1]

print(*dp[K])