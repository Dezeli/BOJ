# 기타줄
import sys

input = sys.stdin.readline

N, M = map(int, input().split())


min_p = 1000
min_o = 1000
for _ in range(M):
    p, o = map(int, input().split())
    min_p = min(p, min_p)
    min_o = min(o, min_o)

if min_o*6 < min_p:
    print(N*min_o)
else:
    if min_o*(N%6)<min_p or N%6==0:
        print(min_p*(N//6)+min_o*(N%6))
    else:
        print(min_p*(N//6+1))