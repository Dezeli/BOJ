# 수도요금
import sys

A = int(sys.stdin.readline().rstrip())
B = int(sys.stdin.readline().rstrip())
C = int(sys.stdin.readline().rstrip())
D = int(sys.stdin.readline().rstrip())
P = int(sys.stdin.readline().rstrip())

if C - P >= 0:
    C = 0
else:
    C = P - C

print(min([B + C * D, A * P]))
