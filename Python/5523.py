# 경기 결과
import sys

input = sys.stdin.readline

N = int(input())

A = 0
B = 0

for _ in range(N):
    a, b = map(int, input().split())

    if a>b:
        A += 1
    if b>a:
        B += 1
print(A, B)