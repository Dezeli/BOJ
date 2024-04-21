# 행렬 곱셈 순서
import sys

input = sys.stdin.readline

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]

for i in range(1, N):
    for s in range(N):
        if s+i == N:
            break

        dp[s][s+i] = int(1e9)
        for t in range(s, s+i):
            dp[s][s+i] = min(dp[s][s+i], dp[s][t]+dp[t+1][s+i]+arr[s][0]*arr[t][1]*arr[s+i][1])

print(dp[0][N-1])