# 별 찍기 - 21

N = int(input())

for i in range(N):
    if N % 2 == 1:
        print("* " * (N // 2 + 1))
        print(" ", end="")
        print("* " * (N // 2 - 1), end="")
    else:
        print("* " * (N // 2))
        print(" ", end="")
        print("* " * (N // 2 - 1), end="")
    if N > 1:
        print("*")
