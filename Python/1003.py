# 피보나치 함수
import sys

T = int(sys.stdin.readline())


def fibonacci(num):
    if num == 0 or num == 1:
        return num
    elif num == -1:
        return 1
    if num == 10:
        return 55
    elif num == 11:
        return 89
    elif num == 20:
        return 6765
    elif num == 21:
        return 10946
    elif num == 30:
        return 832040
    elif num == 31:
        return 1346269
    return fibonacci(num - 1) + fibonacci(num - 2)


for i in range(T):
    num = int(sys.stdin.readline())
    print(fibonacci(num - 1), fibonacci(num))
