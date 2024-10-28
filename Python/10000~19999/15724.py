# 주지수
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

p_sum = [[0 for _ in range(M + 1)]]

for _ in range(N):
    l = list(map(int, input().split()))
    p = [0]
    for i in range(M):
        p.append(l[i] + p_sum[-1][i + 1] + p[-1] - p_sum[-1][i])
    p_sum.append(p)

K = int(input())
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    print(p_sum[x2][y2] - p_sum[x1 - 1][y2] - p_sum[x2][y1 - 1] + p_sum[x1 - 1][y1 - 1])
