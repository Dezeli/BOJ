# 1, 2, 3 더하기 4
import sys

input = sys.stdin.readline

dp = [[1, 0, 0] for _ in range(10005)]
dp[1] = [1, 0, 0]
dp[2] = [1, 1, 0]
dp[3] = [1, 1, 1]

for i in range(4, 10001):
    dp[i][1] = dp[i-2][0] + dp[i-2][1]
    dp[i][2] = sum(dp[i-3])

T = int(input())
for _ in range(T):
    n = int(input())
    print(sum(dp[n]))