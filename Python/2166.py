# 다각형의 면적
import sys

input = sys.stdin.readline

N = int(input())

dots = []
result = 0

for _ in range(N):
    x, y = map(int, input().split())
    dots.append([x, y])

dots.append(dots[0])

for i in range(N):
    result += dots[i][0] * dots[i + 1][1]
    result -= dots[i][1] * dots[i + 1][0]

print(abs(result / 2))
