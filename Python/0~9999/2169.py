# 로봇 조종하기
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dp = []

for _ in range(N):
    dp.append(list(map(int, input().split())))

for j in range(1, M):
    dp[0][j] += dp[0][j-1]

for i in range(1, N):
    go_right = dp[i][:]
    go_left = dp[i][:]

    for j in range(M):
        if j == 0:
            go_right[j] += dp[i-1][j]
        else:
            go_right[j] += max(dp[i-1][j], go_right[j-1])


    for j in range(M-1, -1, -1):
        if j == M - 1:
            go_left[j] += dp[i-1][j]
        else:
            go_left[j] += max(dp[i-1][j], go_left[j+1])

    for j in range(M):
        dp[i][j] = max(go_right[j], go_left[j])

print(dp[N-1][M-1])