# 전투 드로이드 가격

price = [350.34, 230.90, 190.55, 125.30, 180.90]
T = int(input())

for _ in range(T):
    sum_price = 0

    parts = list(map(int, input().split()))
    for i in range(5):
        sum_price += price[i] * parts[i]

    print("${:.2f}".format(sum_price))
