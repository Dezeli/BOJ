# 본대 산책2
import sys

input = sys.stdin.readline


MOD = 1000000007

def multiply(a, b):
    result = []

    for i in range(8):
        line = []
        for j in range(8):
            line.append(sum(a[i][k]*b[k][j]%MOD for k in range(8)) % MOD)
        result.append(line)
    
    return result


roads = [[0, 1, 1, 0, 0, 0, 0, 0],
         [1, 0, 1, 1, 0, 0, 0, 0],
         [1, 1, 0, 1, 1, 0, 0, 0],
         [0, 1, 1, 0, 1, 1, 0, 0],
         [0, 0, 1, 1, 0, 1, 1, 0],
         [0, 0, 0, 1, 1, 0, 0, 1],
         [0, 0, 0, 0, 1, 0, 0, 1],
         [0, 0, 0, 0, 0, 1, 1, 0]
         ]

dp = [[0]*8 for _ in range(8)]

for i in range(8):
    dp[i][i] = 1

D = int(input())

while D > 0:
    if D%2!=0:
        dp = multiply(dp, roads)
        D -= 1
    roads = multiply(roads, roads)
    D //= 2

print(dp[0][0])
