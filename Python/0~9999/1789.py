# 수들의 합
import sys

input = sys.stdin.readline

S = int(input())

cnt = 0
for i in range(1, S+1):
    if i<=S:
        cnt += 1
        S -= i
    else:
        break
print(cnt)