# 별 찍기 - 20
import sys

input = sys.stdin.readline

N = int(input())

for i in range(N):
    if i%2==0:
        print("*"+" *"*(N-1))
    else:
        print(" *"*N)