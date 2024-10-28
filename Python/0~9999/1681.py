# Cow Counting
import sys

N, L = map(int, sys.stdin.readline().split())

num = 0
while N > 0:
    num += 1
    while str(L) in str(num):
        num += 1
    N -= 1

print(num)
