# 신입 사원
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    scores = [list(map(int, input().split())) for _ in range(N)]
    scores.sort()
    min_j = N+1
    cnt = 0
    for i, j in scores:
        if j<min_j:
            cnt += 1
        min_j = min(min_j, j)
    print(cnt)