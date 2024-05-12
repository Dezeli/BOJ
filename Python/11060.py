# 점프 점프
import sys

input = sys.stdin.readline

N = int(input())
maze = list(map(int, input().split()))
dp = [N + 1 for _ in range(N)]
dp[0] = 0

for i in range(N):
    for j in range(i + 1, i + maze[i] + 1):
        if j >= N:
            break
        dp[j] = min(dp[j], dp[i] + 1)

if dp[N - 1] < N + 1:
    print(dp[N - 1])
else:
    print(-1)
