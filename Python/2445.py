# 별 찍기 - 8
import sys

input = sys.stdin.readline

N = int(input())

for i in range(1, N):
    print("*" * i + " " * ((N - i) * 2) + "*" * i)

for i in range(N, 0, -1):
    print("*" * i + " " * ((N - i) * 2) + "*" * i)
