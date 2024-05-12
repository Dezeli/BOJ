# Baskets of Gold Coins

while True:
    try:
        N, w, d, total = map(int, input().split())

        sum = N * (N - 1) // 2 * w
        x = (sum - total) // d
        if x:
            print(x)
        else:
            print(N)
    except:
        break
