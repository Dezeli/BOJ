# 소수
import sys
import math

input = sys.stdin.readline

M = int(input())
N = int(input())


def is_prime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


sum_p = 0
min_p = 0

for i in range(M, N + 1):
    if is_prime(i):
        sum_p += i
        if min_p == 0:
            min_p = i

if sum_p != 0:
    print(sum_p)
    print(min_p)
else:
    print(-1)
