# 예산
import sys

input = sys.stdin.readline

N = int(input())
requests = list(map(int, input().split()))
M = int(input())
l = 0
r = max(requests)

while l <= r:
    mid = (l + r) // 2
    total = 0
    for i in requests:
        if i > mid:
            total += mid
        else:
            total += i
    if total <= M:
        l = mid + 1
    else:
        r = mid - 1
print(r)
