# Σ
import sys
import math

input = sys.stdin.readline
X = 1000000007

def get_val(n, s):
    return s * square(n, X-2) % X


def square(num, s):
    if s == 1:
        return num

    if s % 2 == 0:
        half = square(num, s//2)
        return half * half % X
    else:
        return num * square(num, s - 1) % X


M = int(input())

sum = 0
for _ in range(M):
    n, s = map(int, input().split())
    gcd = math.gcd(n, s)
    n //= gcd
    s //= gcd

    sum += get_val(n, s)
    sum %= X

print(sum)