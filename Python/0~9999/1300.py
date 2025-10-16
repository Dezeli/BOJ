# K번째 수
import sys

input = sys.stdin.readline

N = int(input())
K = int(input())

l = 1
r = N*N

def less_equal_than(a):
    cnt = 0
    for i in range(1, N+1):
        cnt += min(a//i, N)
    return cnt

while l <= r:
    mid = (l + r)//2
    cnt = less_equal_than(mid)

    if cnt>=K:
        answer = mid
        r = mid - 1
    else:
        l = mid + 1


print(answer)