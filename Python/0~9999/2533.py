# 사회망 서비스(SNS)
import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**9)


def dfs(v):
    visit[v] = True
    for n in lines[v]:
        if visit[n]:
            continue
        dfs(n)
        dp[v][0] += dp[n][1]
        dp[v][1] += min(dp[n])


N = int(input())
lines = [[] for _ in range(N + 1)]
visit = [False] * (N + 1)

dp = [[0, 1] for _ in range(N + 1)]

for _ in range(N - 1):
    u, v = map(int, input().split())
    lines[u].append(v)
    lines[v].append(u)

dfs(1)
print(min(dp[1]))
