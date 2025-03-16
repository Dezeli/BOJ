# 도서관
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

l = list(map(int, input().split()))
l.sort()

if abs(l[0]) > abs(l[-1]):
    cnt = -abs(l[0])
else:
    cnt = -abs(l[-1])

for i in range(0, N, M):
    if l[i]<0:
        cnt += abs(l[i])*2
    else:
        break

for i in range(N-1, -1, -M):
    if l[i]>0:
        cnt += l[i]*2
    else:
        break

print(cnt)