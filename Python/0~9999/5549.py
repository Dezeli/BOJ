# 행성 탐사
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
K = int(input())

p_sum = [[[0, 0, 0] for _ in range(M + 1)]]

for _ in range(N):
    l = input().rstrip()
    p = [[0, 0, 0]]
    for i in range(M):
        next = [0, 0, 0]
        for j in range(3):
            next[j] += p[-1][j]
            next[j] += p_sum[-1][i + 1][j]
            next[j] -= p_sum[-1][i][j]
        if l[i] == "J":
            next[0] += 1
        elif l[i] == "O":
            next[1] += 1
        else:
            next[2] += 1
        p.append(next)
    p_sum.append(p)

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    ans = []
    for i in range(3):
        ans.append(
            p_sum[x2][y2][i]
            - p_sum[x1 - 1][y2][i]
            - p_sum[x2][y1 - 1][i]
            + p_sum[x1 - 1][y1 - 1][i]
        )
    print(*ans)
