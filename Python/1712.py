# 손익 분기점
import sys

A, B, C = map(int, (sys.stdin.readline().rstrip()).split(" "))
if B >= C:
    print("-1")
else:
    result = A // (C - B) + 1
    print(result)
