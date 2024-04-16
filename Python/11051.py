# 이항 계수 2
import sys

input = sys.stdin.readline

N, K = map(int, input().split())

ans = 1
for i in range(K):
    ans *= N
    N -= 1

div = 1
for i in range(2, K+1):
    div *= i

print((ans//div)%10007)