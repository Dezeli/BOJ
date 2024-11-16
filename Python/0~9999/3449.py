# 해밍 거리
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    a = input().rstrip()
    b = input().rstrip()
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1

    print(f"Hamming distance is {cnt}.")
