# 쉽게 푸는 문제
import sys

A, B = map(int, sys.stdin.readline().split())

num = 1
num_sum = 0

check = 1

while check <= B:
    for i in range(num):
        if A <= check <= B:
            num_sum += num
        check += 1
    num += 1

print(num_sum)
