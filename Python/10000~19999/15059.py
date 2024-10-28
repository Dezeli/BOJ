# Hard choice
import sys

A1, B1, C1 = map(int, sys.stdin.readline().split())
A2, B2, C2 = map(int, sys.stdin.readline().split())
result = 0
if A1 < A2:
    result += A2 - A1
if B1 < B2:
    result += B2 - B1
if C1 < C2:
    result += C2 - C1
print(result)
