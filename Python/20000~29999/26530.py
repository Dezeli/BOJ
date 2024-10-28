# Shipping

n = int(input())

for _ in range(n):
    x = int(input())
    sum_price = 0
    for __ in range(x):
        product, amount, price = input().split()
        sum_price += float(amount) * float(price)
    result = round(sum_price, 2)
    print("${:.2f}".format(result))
