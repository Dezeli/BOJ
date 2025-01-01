# 찐 Even Number
import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**5)

Q = int(input())

MOD = 10**9 + 7

def mul(n):
    if n==1:
        return 5
    
    if n%2==1:
        return mul(n//2)**2*5%MOD
    else:
        return mul(n//2)**2%MOD

for _ in range(Q):
    N = int(input())
    if N==1:
        print(5)
    else:
        print(4*mul(N-1)%MOD)