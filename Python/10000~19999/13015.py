# 별 찍기 - 23
import sys

input = sys.stdin.readline

N = int(input())

stars = [[" "] * (N * 4 - 3) for i in range(N)]

for i in range(N):
    if i == 0:
        r1 = 0
        r2 = N - 1
        l1 = N * 3 - 3
        l2 = N * 4 - 4
        for j in range(r1, r2 + 1):
            stars[i][j] = "*"
        for j in range(l1, l2 + 1):
            stars[i][j] = "*"
    else:
        r1 += 1
        r2 += 1
        l1 -= 1
        l2 -= 1
        stars[i][r1] = "*"
        stars[i][r2] = "*"
        stars[i][l1] = "*"
        stars[i][l2] = "*"

for line in stars:
    print("".join(line).rstrip())
for line in stars[::-1][1:]:
    print("".join(line).rstrip())
