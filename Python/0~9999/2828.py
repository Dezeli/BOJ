# 사과 담기 게임
import sys

sys.stdin.readline

N, M = map(int, input().split())
J = int(input())
l = 1
r = M

cnt = 0
for _ in range(J):
    i = int(input())
    if l<=i<=r:
        continue
    if i<l:
        cnt += l-i
        l = i
        r = l+M-1
    else:
        cnt += i-r
        r = i
        l = r-M+1

print(cnt)
