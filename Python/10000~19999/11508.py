# 2+1 세일
import sys

input = sys.stdin.readline

N = int(input())
C = [int(input()) for _ in range(N)]
C.sort(reverse=True)

price = 0
for i in range(N):
    if i % 3 == 2:
        continue
    price += C[i]

print(price)
