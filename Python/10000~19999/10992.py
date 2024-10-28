# 별 찍기 - 17

import sys

input = sys.stdin.readline

N = int(input())

for i in range(N):
    if i == 0:
        print(" " * (N - i - 1) + "*")
    elif i == N - 1:
        print("*" * (i * 2 + 1))
    else:
        print(" " * (N - i - 1) + "*" + " " * (i * 2 - 1) + "*")
