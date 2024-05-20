# 학식 사주기
import sys

input = sys.stdin.readline

N = int(input())
A = [int(input()) for _ in range(N)]

M = int(input())
price = [A[int(input())-1] for _ in range(M)]

print(sum(price))