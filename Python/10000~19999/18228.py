# 펭귄추락대책위원회
import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
i = A.index(-1)

print(min(A[:i]) + min(A[i + 1 :]))
