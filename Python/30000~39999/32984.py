# 겨울이 좋아
import sys

input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
max_leaf = 0
winter = {}

for i in range(N):
    a = A[i]
    b = B[i]
    if a % b == 0:
        winter[a // b] = 1 + winter.get(a // b, 0)
        max_leaf = max(max_leaf, a // b)
    else:
        winter[a // b + 1] = 1 + winter.get(a // b, 0)
        max_leaf = max(max_leaf, a // b + 1)

l = 0
sum_l = 0
for i in range(max_leaf, 0, -1):
    l += winter.get(i, 0)
    sum_l += l
    if sum_l > i - 1:
        print(i)
        break
