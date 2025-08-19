# 공유기 설치
import sys

input = sys.stdin.readline

N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]
houses.sort()
l = 1
r = houses[-1] - houses[0]

def check_avail(d):
    last = houses[0]
    cnt = 1
    i = 1
    while i < N:
        if houses[i]-last>=d:
            last = houses[i]
            cnt += 1
        i += 1
        if cnt >= C:
            return True
        if i >= N:
            return False

while l<r:
    mid = (l+r+1)//2
    if check_avail(mid):
        l = mid
    else:
        r = mid -1
    
print(l)