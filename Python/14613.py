# 너의 티어는?
import sys

input = sys.stdin.readline

W, L, D = map(float, input().split())

dp = [[0] * 41 for _ in range(21)]
dp[0][20] = 1

for i in range(20):
    for j in range(41):
        if dp[i][j]:
            dp[i + 1][j - 1] += dp[i][j] * L
            dp[i + 1][j] += dp[i][j] * D
            dp[i + 1][j + 1] += dp[i][j] * W

print(format(round(sum(dp[20][0:10]), 8), ".8f"))
print(format(round(sum(dp[20][10:20]), 8), ".8f"))
print(format(round(sum(dp[20][20:30]), 8), ".8f"))
print(format(round(sum(dp[20][30:40]), 8), ".8f"))
print(format(round(dp[20][40], 8), ".8f"))
