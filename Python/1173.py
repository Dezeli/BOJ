# 운동
import sys

N, m, M, T, R = map(int, sys.stdin.readline().split())
E = 0
time = 0
cur = m
if M < m + T:
    print(-1)
else:
    while E != N:
        time += 1
        if M >= cur + T:
            E += 1
            cur += T
        else:
            rest = (cur + T - M) // R
            for i in range(rest - 1):
                time += 1
                cur = cur - R
            cur = max(m, cur - R)
    print(time)
