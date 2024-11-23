# 본대 산책 3
import sys

input = sys.stdin.readline

MOD = 1000000007
n, m = map(int, input().split())


def multiply(a, b):
    result = []

    for i in range(n):
        line = []
        for j in range(n):
            line.append(sum(a[i][k]*b[k][j]%MOD for k in range(n)) % MOD)
        result.append(line)
    
    return result


roads = [[0]*n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    roads[a-1][b-1] = 1
    roads[b-1][a-1] = 1


dp = [[0]*n for _ in range(n)]
for i in range(n):
    dp[i][i] = 1

D = int(input())

while D > 0:
    if D%2!=0:
        dp = multiply(dp, roads)
        D -= 1
    roads = multiply(roads, roads)
    D //= 2

print(dp[0][0])
