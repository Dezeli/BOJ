# 꼬리를 무는 숫자 나열
import sys

A, B = map(int, sys.stdin.readline().split())

A1, A2 = divmod(A, 4)
B1, B2 = divmod(B, 4)
if A2 == 0:
    A2 = 4
    A1 -= 1
if B2 == 0:
    B2 = 4
    B1 -= 1

print(abs(A1 - B1) + abs(A2 - B2))
