# 오버플로우와 모듈러
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

l = 1
for i in list(map(int, input().split())):
    l *= i
    l %= M
print(l)
