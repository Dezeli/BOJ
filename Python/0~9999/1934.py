# 최소공배수
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    aa, bb = a, b

    while a % b != 0:
        a, b = b, a % b

    print(aa * bb // b)
