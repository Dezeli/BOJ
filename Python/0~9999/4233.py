# 소수 구하기
import sys

input = sys.stdin.readline


def isPrime(n):
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            return False
    return True

def power(a, p):
    MOD = p
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


while True:
    p, a = map(int, input().split())
    if p == a == 0:
        break
    if not isPrime(p) and power(a, p) == a:
        print("yes")
    else:
        print("no")