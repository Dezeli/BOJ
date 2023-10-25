# Volta
# 포르투갈어 문제
import sys

F, S = map(int, sys.stdin.readline().split())
num = 2
while 1 / F * (num - 1) < 1 / S * num:
    num += 1
print(num)
