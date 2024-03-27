# 로프
import sys

input = sys.stdin.readline

N = int(input())

ropes = [int(input()) for _ in range(N)]
ropes.sort()
max_bear = 0
cnt = N
for i in ropes:
    max_bear = max(max_bear, i*cnt)
    cnt -= 1

print(max_bear)