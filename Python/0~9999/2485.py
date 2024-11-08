# 가로수
import sys
import math

input = sys.stdin.readline

N = int(input())

d = []

first = int(input())
last = first
for _ in range(N - 1):
    cur = int(input())
    d.append(last - cur)
    last = cur

gcd = math.gcd(d[0], d[1])
for i in range(2, N - 1):
    gcd = math.gcd(gcd, d[i])

print((last - first) // gcd - N + 1)
