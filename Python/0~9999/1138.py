# 한 줄로 서기
import sys

input = sys.stdin.readline

N = int(input())
h = list(map(int, input().split()))

line = [0 for _ in range(N)]

for i in range(N):
    p = h[i]
    cnt = 0
    idx = 0
    while cnt != p:
        if line[idx] == 0:
            cnt += 1
        idx += 1
    while line[idx] != 0:
        idx += 1

    line[idx] = i + 1

print(*line)
