# APC는 왜 서브태스크 대회가 되었을까?
import sys

input = sys.stdin.readline

N, L, K = map(int, input().split())

s1_cnt = 0
s2_cnt = 0

for _ in range(N):
    s1, s2 = map(int, input().split())
    if s2 <= L:
        s2_cnt += 1
    else:
        if s1 <= L:
            s1_cnt += 1

if s2_cnt >= K:
    print(140 * K)
else:
    print(140 * s2_cnt + 100 * (min(s1_cnt, K - s2_cnt)))
