# 기타리스트
import sys

input = sys.stdin.readline

N, S, M = map(int, input().split())
songs = list(map(int, input().split()))

dp = [[0]*(M+1) for _ in range(N+1)]
dp[0][S] = 1

for i in range(N):
    for j in range(M+1):
        if dp[i][j] == 1:
            if j+songs[i] <= M:
                dp[i+1][j+songs[i]] = 1
            if j-songs[i] >= 0:
                dp[i+1][j-songs[i]] = 1

ans = -1
for i in range(M, -1, -1):
    if dp[N][i]==1:
        ans = i
        break
print(ans)