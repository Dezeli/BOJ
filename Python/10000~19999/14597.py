# Quilting (Large)
import sys

input = sys.stdin.readline

H, W = map(int, input().split())

B1 = [list(map(int, input().split())) for _ in range(H)]
B2 = [list(map(int, input().split())) for _ in range(H)]


if W == 1:
    result = 0
    for i in range(H):
        result += (B1[i][0] - B2[i][0]) ** 2
    print(result)
else:
    dp = [[0] * W for _ in range(H)]
    for i in range(W):
        dp[0][i] = (B1[0][i] - B2[0][i]) ** 2

    for i in range(1, H):
        dp[i][0] = min(dp[i - 1][0], dp[i - 1][1]) + (B1[i][0] - B2[i][0]) ** 2
        for j in range(1, W - 1):
            dp[i][j] = (
                min(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1])
                + (B1[i][j] - B2[i][j]) ** 2
            )
        dp[i][W - 1] = (
            min(dp[i - 1][W - 2], dp[i - 1][W - 1]) + (B1[i][W - 1] - B2[i][W - 1]) ** 2
        )

    print(min(dp[-1]))
