# 흙길 보수하기
import sys

input = sys.stdin.readline

N, L = map(int, input().split())

water = []
for _ in range(N):
    s, e = map(int, input().split())
    water.append([s, e])

water.sort()

cnt = 0
last = 0
for s, e in water:
    s = max(last, s)
    
    dif = e-s
    if dif%L==0:
        cnt = cnt + dif//L
    else:
        cnt += dif//L + 1
        last = e + L - dif%L
        
print(cnt)