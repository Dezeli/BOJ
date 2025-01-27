# 신기한 수
import sys

input = sys.stdin.readline
n = int(input())
r = 0

for i in range(1, n + 1):
    s = 0
    n2 = i
    while n2:
        s += n2 % 10
        n2 //= 10

    if i % s == 0:
        r += 1

print(r)
