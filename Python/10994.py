# 별 찍기 - 19
import sys

input = sys.stdin.readline

N = int(input())

stars = [[" "] * (N * 4 - 3) for _ in range(N * 4 - 3)]
for i in range(N * 4 - 3):
    if i % 2 == 0:
        for j in range(i, N * 4 - 3 - i):
            stars[i][j] = "*"
            stars[j][i] = "*"
            stars[N * 4 - 4 - i][j] = "*"
            stars[j][N * 4 - 4 - i] = "*"
    else:
        continue

for line in stars:
    print("".join(line))
