# 전자레인지
import sys

A = int(sys.stdin.readline().rstrip())
B = int(sys.stdin.readline().rstrip())
C = int(sys.stdin.readline().rstrip())
D = int(sys.stdin.readline().rstrip())
E = int(sys.stdin.readline().rstrip())

if A < 0:
    print(abs(A) * C + D + B * E)
else:
    print((B - A) * E)
