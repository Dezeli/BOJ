# Z
import sys

N, r, c = map(int, sys.stdin.readline().split())

multiply = 1
cnt = 0
while r != 0 or c != 0:
    c, remain = divmod(c, 2)
    cnt += multiply * remain
    multiply *= 2
    r, remain = divmod(r, 2)
    cnt += multiply * remain
    multiply *= 2

print(cnt)
