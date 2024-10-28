# 별 찍기 - 2

N = int(input())

for i in range(N):
    print(" " * (N - (i + 1)), end="")
    print("*" * (i + 1))
