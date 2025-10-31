# 경찰차
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
W = int(input())

INF = 10**7
dp = [[INF]*(W+1) for _ in range(W+1)]
dp[0][0] = 0
parent = {}

cases = [(1, 1)]

def get_dis(car, case_s, case_e):
    if case_s == 0:
        sx, sy = (1, 1) if car == 1 else (N, N)
    else:
        sx, sy = cases[case_s]
    ex, ey = cases[case_e]
    
    return abs(sx-ex) + abs(sy-ey)


for i in range(W):
    x, y = map(int, input().split())
    cases.append((x, y))


for c in range(1, W+1):
    j = c-1
    for k in range(c):
        if dp[c][k] > dp[j][k] + get_dis(1, j, c):
            dp[c][k] = dp[j][k] + get_dis(1, j, c)
            parent[(c, k)] = (j, k)
        
        if dp[j][c] > dp[j][k] + get_dis(2, k, c):
            dp[j][c] = dp[j][k] + get_dis(2, k, c)
            parent[(j, c)] = (j, k)

        if dp[c][j] > dp[k][j] + get_dis(1, k, c):
            dp[c][j] = dp[k][j] + get_dis(1, k, c)
            parent[(c, j)] = (k, j)

        if dp[k][c] > dp[k][j] + get_dis(2, j, c):
            dp[k][c] = dp[k][j] + get_dis(2, j, c)
            parent[(k, c)] = (k, j)


min_dis = INF
last_idx = ()

j = W
for i in range(W):
    if min_dis > dp[i][j]:
        min_dis = dp[i][j]
        last_idx = (i, j)
    if min_dis > dp[j][i]:
        min_dis = dp[j][i]
        last_idx = (j, i)

print(min_dis)

route = []
def backtrack(idx, case):
    if case==0:
        return

    if idx[0]==case:
        route.append(1)
    else:
        route.append(2)
    
    backtrack(parent[idx], case-1)

backtrack(last_idx, W)
for i in route[::-1]:
    print(i)