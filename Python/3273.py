# 두 수의 합
import sys

input = sys.stdin.readline
n = int(input())
a = sorted(list(map(int, input().split())))
x = int(input())

l = 0
r = n - 1
cnt = 0
while l < r:
    if a[l] + a[r] == x:
        cnt += 1
        l += 1
    elif a[l] + a[r] < x:
        l += 1
    else:
        r -= 1
print(cnt)
