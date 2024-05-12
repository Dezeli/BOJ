# 1의 개수 세기
import sys
import math

sys.setrecursionlimit(10**8)
input = sys.stdin.readline


def f(x):
    if x <= 0:
        return 0

    digit = int(math.log2(x))
    base = 2**digit
    if base == x:
        return digit * x // 2 + 1

    diff = x - base
    return f(base) + diff + f(diff)


A, B = map(int, input().split())
print(f(B) - f(A - 1))
