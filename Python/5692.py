# 팩토리얼 진법
import sys

input = sys.stdin.readline


def fac(num):
    if num == 1:
        return 1
    return num * fac(num - 1)


while True:
    num = int(input())
    if num == 0:
        break

    num10 = 0
    i = 1
    while num != 0:
        num10 += fac(i) * (num % 10)
        num = num // 10
        i += 1
    print(num10)
