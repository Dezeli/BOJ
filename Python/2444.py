# 별 찍기 - 7
import sys

input = sys.stdin.readline

N = int(input())

for i in range(N-1, 0, -1):
    print(" "*i+"*"*((N-i)*2-1))

for i in range(N):
    print(" "*i+"*"*((N-i)*2-1))