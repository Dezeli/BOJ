# 개똥벌레
import sys

input = sys.stdin.readline
N, H = map(int, input().split())

suk = [0]*(H+1)
jong = [0]*(H+1)

crash = N
cnt = 0

for i in range(N):
    obs = int(input())
    if i % 2 == 0:
        suk[obs] += 1
    else:
        jong[obs] += 1

for i in range(H-1, 0, -1):
    suk[i] += suk[i+1]
    jong[i] += jong[i+1]

for i in range(1, H+1):
    if crash > (suk[i] + jong[H-i+1]):
        crash = (suk[i] + jong[H-i+1])
        cnt = 1
    elif crash == (suk[i] + jong[H-i+1]):
        cnt += 1

print(crash, cnt)