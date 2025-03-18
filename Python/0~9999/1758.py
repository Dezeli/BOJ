# 알바생 강호
import sys

input = sys.stdin.readline

N = int(input())

line = [int(input()) for _ in range(N)]
line.sort(reverse=True)

tip = 0

for i in range(N):
    tip += max(line[i] - i, 0)

print(tip)
