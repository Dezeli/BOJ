# 주몽
import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
mat = list(map(int, input().split()))

mat.sort()

l = 0
r = N - 1
cnt = 0
while l < r:
    if mat[l] + mat[r] == M:
        cnt += 1
        l += 1
    elif mat[l] + mat[r] < M:
        l += 1
    else:
        r -= 1
print(cnt)
