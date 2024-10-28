# 1학년
import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

dp = [[0] * 21 for _ in range(N - 1)]

dp[0][nums[0]] = 1

for i in range(1, N - 1):
    num = nums[i]
    for j in range(0, 21):
        if j + num < 21:
            dp[i][j + num] += dp[i - 1][j]
        if j - num >= 0:
            dp[i][j - num] += dp[i - 1][j]

print(dp[N - 2][nums[-1]])
