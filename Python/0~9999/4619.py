# 루트

while True:
    B, N = map(int, input().split())

    if B == 0 and N == 0:
        break

    i = 1
    while i**N < B:
        i += 1

    if i**N - B > B - (i - 1) ** N:
        print(i - 1)
    else:
        print(i)
