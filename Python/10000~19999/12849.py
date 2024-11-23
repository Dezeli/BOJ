# 본대 산책
import sys

input = lambda: sys.stdin.readline().rstrip()

graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3, 4],
    3: [1, 2, 4, 5],
    4: [2, 3, 5, 6],
    5: [3, 4, 7],
    6: [4, 7],
    7: [5, 6],
}

D = int(input())

dp = [[0] * 8 for _ in range(D + 1)]

dp[0][0] = 1

for i in range(1, D + 1):
    for j in range(8):
        for n in graph[j]:
            dp[i][n] += dp[i - 1][j]
            dp[i][n] = dp[i][n] % 1000000007

print(dp[-1][0])
