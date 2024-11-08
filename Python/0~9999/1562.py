# 계단 수
import sys

input = sys.stdin.readline

N = int(input())

DP = [[[0] * 1024 for _ in range(10)] for __ in range(N + 1)]

start = 256
for i in range(1, 10):
    DP[1][i][start] += 1
    start = start // 2

move = {
    0: [-1, 256],
    1: [512, 128],
    2: [256, 64],
    3: [128, 32],
    4: [64, 16],
    5: [32, 8],
    6: [16, 4],
    7: [8, 2],
    8: [4, 1],
    9: [2, -1],
}

for i in range(1, N):
    for j in range(10):
        for k in range(1024):
            cur = DP[i][j][k]
            if cur == 0:
                continue
            m1, m2 = move[j]
            if (k // m1) % 2 == 1:
                m1 = 0
            if (k // m2) % 2 == 1:
                m2 = 0
            if j == 0:
                DP[i + 1][1][k + m2] += cur
            elif j == 9:
                DP[i + 1][8][k + m1] += cur
            else:
                DP[i + 1][j - 1][k + m1] += cur
                DP[i + 1][j + 1][k + m2] += cur

cnt = 0
for i in range(10):
    cnt += DP[-1][i][-1]

print(cnt % 1000000000)
