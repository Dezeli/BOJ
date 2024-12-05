# 신기한 수
import sys

n = int(sys.stdin.readline())
sum = 0

for i in range(1, n + 1):
    num = 0
    N = str(i)

    for j in N:
        num = num + int(j)

    if i % num == 0:
        sum = sum + 1

print(sum)
