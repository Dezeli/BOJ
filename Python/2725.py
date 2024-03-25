# 보이는 점의 개수
import sys

input = sys.stdin.readline

def gcd(i, j):
    if j==0:
        return i
    return gcd(j, i % j)

dots = [0 for _ in range(1001)]
dots[1] = 3
for i in range(2, 1001):
    cnt = 0
    for j in range(1, i+1):
        if i==j:
            continue
        if gcd(i, j) == 1:
            cnt += 2
    dots[i] = dots[i-1] + cnt

C = int(input())
for _ in range(C):
    N = int(input())
    print(dots[N])