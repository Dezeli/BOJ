# 양동이 게임
import sys
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())

hoses = defaultdict(list)

for _ in range(M):
    v, w = map(int, input().split())
    hoses[v].append(w)

dp = [[0]*(N+1) for _ in range(M)]
if M!=0:
    dp[0][1] = 100

    for i in range(M-1):
        for j in range(1, N+1):
            if dp[i][j] > 0:
                h = hoses[j]
                if len(h):
                    for k in h:
                        dp[i+1][k] += dp[i][j]/len(h)
                else:
                    dp[i+1][j] += dp[i][j]

    print(max(dp[-1]))
else:
    print(100)