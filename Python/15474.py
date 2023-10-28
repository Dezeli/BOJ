# 鉛筆 (Pencils)
import sys

N, A, B, C, D = map(int, sys.stdin.readline().split())

A_set = N // A
if N % A != 0:
    A_set += 1
C_set = N // C
if N % C != 0:
    C_set += 1
print(min(A_set * B, C_set * D))
