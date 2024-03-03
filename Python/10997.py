# 별 찍기 - 22
import sys
import copy

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
if N != 1:
    stars.insert(N * 2 - 1, copy.deepcopy(stars[N * 2 - 2]))
    stars.insert(N * 2 - 1, copy.deepcopy(stars[N * 2 - 2]))

for i in range(1, 2 * N - 1):
    if i % 2 == 1:
        stars[i][len(stars[0]) - i] = " "
    else:
        stars[i][len(stars[0]) - i] = "*"


for line in range(len(stars)):
    if line == 1:
        print("*")
    else:
        print("".join(stars[line]))
