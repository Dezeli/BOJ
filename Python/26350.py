# Good Coin Denomination

d = int(input())

for _ in range(d):
    coins = list(map(int, input().split()))[1:]
    print("Denominations: ", end="")
    print(*coins)

    last = 0
    good = True
    for i in coins:
        if i < last * 2:
            good = False
            break
        last = i
    if good:
        print("Good coin denominations!")
    else:
        print("Bad coin denominations!")
    print()
