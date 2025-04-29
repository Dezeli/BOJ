# 양 한마리... 양 A마리... 양 A제곱마리...
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

A, B = map(int, input().split())

MOD = 1000000007

def power(a, p):
    num = 1
    while p:
        if p & 1 == 1:
            num *= a
            num %= MOD
        p >>= 1
        a **= 2
        a %= MOD
    num %= MOD
    return num

if A==1:
    print(B%MOD)
else:
    print((power(A, B)-1)*power(A-1, MOD-2)%MOD)