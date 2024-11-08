# 두 배 더하기
import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

max_mul = 0
sum_plus = 0

for num in A:
    mul = 0
    while num:
        if num % 2 == 0:
            num = num // 2
            mul += 1
        else:
            num -= 1
            sum_plus += 1
    max_mul = max(max_mul, mul)

print(max_mul + sum_plus)
