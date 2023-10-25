# Do Not Touch Anything
import sys

R, C, N = map(int, sys.stdin.readline().split())
x = R // N
if R % N != 0:
    x += 1
y = C // N
if C % N != 0:
    y += 1
print(x * y)
