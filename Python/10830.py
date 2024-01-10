# 행렬 제곱
import sys
input = sys.stdin.readline

N, B = map(int, input().split())
A = [[*map(int, input().split())] for _ in range(N)]

def mul(U, V):
    len_U = len(U)
    new_mat = [[0]*len_U for _ in range(len_U)]
    
    for row in range(len_U):
        for col in range(len_U):
            new_num = 0
            for i in range(len_U):
                new_num += U[row][i] * V[i][col]
            new_mat[row][col] = new_num % 1000

    return new_mat

def square(A, size):
    if size == 1:
        for x in range(len(A)):
            for y in range(len(A)):
                A[x][y] %= 1000
        return A
    
    tmp = square(A, size//2)
    if size % 2:
        return mul(mul(tmp, tmp), A)
    else:
        return mul(tmp, tmp)

result = square(A, B)
for r in result:
    print(*r)