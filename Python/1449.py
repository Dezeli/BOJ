# 수리공 항승
import sys

input = sys.stdin.readline

N, L = map(int, input().split())
pipes = list(map(int, input().split()))

cnt = 0
pipes.sort()

block = [False for _ in range(1001+L)]

for i in pipes:
    if block[i]:
        continue
    cnt += 1
    for j in range(L):
        block[i+j] = True

print(cnt)