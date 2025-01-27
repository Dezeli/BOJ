# GCD(n, k) = 1
import sys

input = sys.stdin.readline

n = int(input())
cnt = n

for i in range(2, int(n ** (1 / 2)) + 1):
    if n % i == 0:
        while n % i == 0:
            n //= i
        cnt = cnt - (cnt / i)

if n > 1:
    cnt *= 1 - 1 / n

print(int(cnt))
