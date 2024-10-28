# 피자판매
import sys
from collections import defaultdict

input = sys.stdin.readline


A_pizza = defaultdict(int)
B_pizza = defaultdict(int)

P = int(input())
m, n = map(int, input().split())

A_slice = []
B_slice = []
for _ in range(m):
    A_slice.append(int(input()))
for _ in range(n):
    B_slice.append(int(input()))

for i in range(m):
    sum_slice = A_slice[i]
    A_pizza[sum_slice] += 1
    for j in range(1, m - 1):
        sum_slice += A_slice[(i + j) % m]
        A_pizza[sum_slice] += 1
A_pizza[sum(A_slice)] += 1
A_pizza[0] += 1

for i in range(n):
    sum_slice = B_slice[i]
    B_pizza[sum_slice] += 1
    for j in range(1, n - 1):
        sum_slice += B_slice[(i + j) % n]
        B_pizza[sum_slice] += 1
B_pizza[sum(B_slice)] += 1
B_pizza[0] += 1

cnt = 0
for s, c in A_pizza.items():
    if s > P:
        continue
    cnt += c * B_pizza[P - s]
print(cnt)
