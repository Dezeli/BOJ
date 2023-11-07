# 파도반 수열
import sys

T = int(sys.stdin.readline().rstrip())

Ps = [0, 1, 1, 1]
for i in range(1, 100):
    Ps.append(Ps[i]+Ps[i+1])

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    print(Ps[N])
