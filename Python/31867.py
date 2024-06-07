# 홀짝홀짝
import sys

input = sys.stdin.readline

N = int(input())
K = input().rstrip()


num = 0
for i in K:
    if int(i)%2==0:
        num += 1
    else:
        num -= 1


if num==0:
    print(-1)
elif num>0:
    print(0)
else:
    print(1)