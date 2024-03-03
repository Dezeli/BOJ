# RGB거리 2
import sys

input = sys.stdin.readline

N = int(input())
house_rgb = [list(map(int, input().split())) for _ in range(N)]

INF = 2e9
ans = INF

for i in range(3):
    dp = [[INF] * 3 for _ in range(N)]
    dp[0][i] = house_rgb[0][i]
    for j in range(1, N):
        dp[j][0] = house_rgb[j][0] + min(dp[j - 1][1], dp[j - 1][2])
        dp[j][1] = house_rgb[j][1] + min(dp[j - 1][0], dp[j - 1][2])
        dp[j][2] = house_rgb[j][2] + min(dp[j - 1][0], dp[j - 1][1])
    for k in range(3):
        if i != k:
            ans = min(ans, dp[-1][k])
print(ans)
