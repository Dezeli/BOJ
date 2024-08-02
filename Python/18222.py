# 투에-모스 문자열
import sys

input = sys.stdin.readline

k = int(input())

sqrs = [2**(59-i) for i in range(59)]

cnt = 0
for i in sqrs:
    if k-i > 0:
        k -= i
        cnt += 1

if k==1:
    if cnt%2==0:
        print(0)
    else:
        print(1)
else:
    if cnt%2==0:
        print(1)
    else:
        print(0)