# 피자 (Large)
import sys

sys.setrecursionlimit(10**5)
input = sys.stdin.readline


def divide(P):
    if P == 1:
        return 0
    if P == 2:
        return 1

    if P % 2 == 1:
        return divide(P // 2) + divide(P // 2 + 1) + (P // 2) * (P // 2 + 1)
    else:
        return divide(P // 2) * 2 + (P // 2) ** 2


N = int(input())
print(divide(N))
