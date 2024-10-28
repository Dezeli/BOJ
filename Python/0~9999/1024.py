# 수열의 합
import sys


def sum_suyeol(N, L):
    while L < 101:
        first_num = N / L - (L - 1) / 2
        if first_num == int(first_num) and first_num >= 0:
            return [int(first_num) + i for i in range(L)]
        L += 1
    return -1


N, L = map(int, sys.stdin.readline().split())
result = sum_suyeol(N, L)
if result != -1:
    for i in result[0:-1]:
        print(i, end=" ")
    print(result[-1])
else:
    print(result)
