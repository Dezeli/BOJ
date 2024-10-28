# Enigmatic Device
import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())

for _ in range(m):
    k, l, r = map(int, input().split())
    if k == 2:
        print(sum([a[i] for i in range(l - 1, r)]))
    else:
        for i in range(l - 1, r):
            a[i] = a[i] ** 2 % 2010
