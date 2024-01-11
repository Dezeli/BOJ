# 플로이드
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

inf = int(1e9)
buses = [[inf]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    buses[i][i] = 0

for _ in range(m):
    i, j, cost = map(int, input().split())
    buses[i][j] = min([buses[i][j], cost])

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            buses[i][j] = min(buses[i][j], buses[i][k] + buses[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if buses[i][j] == inf:
            print("0",  end=" ")
        else:
            print(buses[i][j], end=" ")
    print()