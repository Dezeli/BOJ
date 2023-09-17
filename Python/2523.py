# 별 찍기 - 13

N = int(input())

if N != 1:
    for i in range(N):
        print("*" * (i + 1), end=" \n")

    for i in range(1, N - 1):
        print("*" * (N - i), end="\n")
print("*", end="")
