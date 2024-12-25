# 2017 아주대학교 프로그래밍 경시대회 (Large)
import sys

input = sys.stdin.readline

N = int(input())

p = []

for i in range(1, N+1):
    S, C, L = map(int, input().split())
    p.append([-S, C, L, i])

p.sort()
print(p[0][-1])
