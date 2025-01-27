# 거스름돈
import sys

input = sys.stdin.readline

N = 1000 - int(input())

cnt = 0
money = [500, 100, 50, 10, 5, 1]
for m in money:
    c = N // m
    N -= m * c
    cnt += c

print(cnt)
