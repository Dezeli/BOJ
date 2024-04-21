# 점프
import sys

input = sys.stdin.readline

N = int(input())
game = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        plus = game[i][j]
        if plus==0:
            continue
        if i+plus<N:
            dp[i+plus][j] += dp[i][j]
        if j+plus<N:
            dp[i][j+plus] += dp[i][j]

print(dp[N-1][N-1])