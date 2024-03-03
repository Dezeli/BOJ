# 파이프 옮기기 1
import sys

input = sys.stdin.readline
N = int(input())
pipe_map = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]
# dp[0] -> 가로, dp[1] -> 대각선, dp[2] -> 세로


def move_pipe():
    dp[0][0][1] = 1
    for i in range(2, N):
        if pipe_map[0][i] == 0:
            dp[0][0][i] = dp[0][0][i - 1]

    for r in range(1, N):
        for c in range(1, N):
            if (
                pipe_map[r][c] == 0
                and pipe_map[r][c - 1] == 0
                and pipe_map[r - 1][c] == 0
            ):
                dp[1][r][c] = (
                    dp[0][r - 1][c - 1] + dp[1][r - 1][c - 1] + dp[2][r - 1][c - 1]
                )

            if pipe_map[r][c] == 0:
                dp[0][r][c] = dp[0][r][c - 1] + dp[1][r][c - 1]
                dp[2][r][c] = dp[2][r - 1][c] + dp[1][r - 1][c]

    print(sum(dp[i][N - 1][N - 1] for i in range(3)))


move_pipe()
