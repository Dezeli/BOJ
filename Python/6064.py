# 카잉 달력
from sys import stdin

T = int(stdin.readline().rstrip())

def find(M, N, x, y):
    k = x
    while k <= M * N:
        if (k - x) % M == 0 and (k - y) % N == 0:
            return k
        k += M
    return -1


for _ in range(T):
    M, N, x, y = map(int, stdin.readline().split(" "))
    print(find(M, N, x, y))