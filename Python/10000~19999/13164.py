# 행복 유치원
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
line = list(map(int, input().split()))

dif = []
for i in range(N - 1):
    dif.append(line[i + 1] - line[i])

dif.sort()
for i in range(K - 1):
    dif.pop()

print(sum(dif))
