# 문자열 집합
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

S = set()
for _ in range(N):
    S.add(input())
cnt = 0
for _ in range(M):
    t = input()
    if t in S:
        cnt+=1
print(cnt)