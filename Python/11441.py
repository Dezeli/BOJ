# 합 구하기
import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

sum_A = [0]
for i in A:
    sum_A.append(sum_A[-1] + i)

M = int(input())
for _ in range(M):
    l, r = map(int, input().split())
    print(sum_A[r]-sum_A[l-1])