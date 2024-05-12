# 기타 레슨
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
lesson = list(map(int, input().split()))

ans = 0
l, r = max(lesson), sum(lesson)
while l <= r:
    mid = (l + r) // 2
    cnt, sum_t = 0, 0
    for i in range(N):
        if sum_t + lesson[i] > mid:
            cnt += 1
            sum_t = 0
        sum_t += lesson[i]
    if sum_t:
        cnt += 1

    if cnt > M:
        l = mid + 1
    else:
        r = mid - 1
        ans = mid

print(ans)
