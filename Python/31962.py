# 등교 
import sys

input = sys.stdin.readline

N, X = map(int, input().split())

max_time = -1
for _ in range(N):
    S, T = map(int, input().split())
    if S+T <= X:
        max_time = max(max_time, S)

print(max_time)