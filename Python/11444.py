# 피보나치 수 6
import sys

input = sys.stdin.readline

n = int(input())
p = 1000000007


def mul(A, B):
    n = 2
    Z = [[0] * 2 for _ in range(2)]

    for row in range(2):
        for col in range(2):
            e = 0
            for i in range(2):
                e += A[row][i] * B[i][col]
            Z[row][col] = e % p
    return Z


def square(A, num):
    if num == 1:
        for x in range(2):
            for y in range(2):
                A[x][y] %= p
        return A

    tmp = square(A, num // 2)
    if num % 2:
        return mul(mul(tmp, tmp), A)
    else:
        return mul(tmp, tmp)


fib_matrix = [[1, 1], [1, 0]]
print(square(fib_matrix, n)[0][1])
