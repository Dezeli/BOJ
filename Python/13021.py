# 공 색칠하기
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

balls = [0 for _ in range(N+1)]

for i in range(1, M+1):
    L, R = map(int, input().split())
    for j in range(L, R+1):
        balls[j] = i

print(2**(len(set(balls))-1))
