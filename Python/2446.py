# 별 찍기 - 9

N = int(input())

if N != 1:
    for i in range(N):
        print(" " * i, end="")
        print("*" * ((N - i) * 2 - 1), end="")
        print("", end=" \n")
    for i in range(1, N - 1):
        print(" " * (N - i - 1), end="")
        print("*" * ((i + 1) * 2 - 1), end="")
        print("", end=" \n")
print("*" * ((N) * 2 - 1), end="")
