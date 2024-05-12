# Walk Like an Egyptian

while True:
    N = int(input())

    if N == 0:
        break

    num = 1
    for i in range(2, 2 * N, 2):
        num += i
    print(f"{N} => {num}")
