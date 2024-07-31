# 소수 최소 공배수
import sys
import math

input = sys.stdin.readline


def is_prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


N = int(input())
nums = list(set(map(int, input().split())))

ans = 1
for i in nums:
    if is_prime(i):
        ans *= i

if ans!=1:
    print(ans)
else:
    print(-1)