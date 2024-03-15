# 두 배열의 합
import sys
from collections import defaultdict

input = sys.stdin.readline

T = int(input())

n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

A_dict = defaultdict(int)
B_dict = defaultdict(int)

for i in range(n):
    sum_li = A[i]
    A_dict[sum_li] += 1
    for j in range(i+1, n):
        sum_li += A[j]
        A_dict[sum_li] += 1

for i in range(m):
    sum_li = B[i]
    B_dict[sum_li] += 1
    for j in range(i+1, m):
        sum_li += B[j]
        B_dict[sum_li] += 1

cnt = 0
for key, val in A_dict.items():
    cnt += B_dict[T-key]*val

print(cnt)