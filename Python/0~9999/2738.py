# 행렬 덧셈

N, M = map(int, input().split())
A = []
B = []

for _ in range(N):
    m = list(map(int, input().split()))
    A.append(m)

for _ in range(N):
    m = list(map(int, input().split()))
    B.append(m)

for i in range(N):
    for j in range(M):
        print(A[i][j] + B[i][j], end="")
        if j != M - 1:
            print(" ", end="")
    print("")
