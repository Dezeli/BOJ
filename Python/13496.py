# The Merchant of Venice

K = int(input())

for i in range(1, K + 1):
    n, s, d = map(int, input().split())

    money = 0
    for __ in range(n):
        di, dv = map(int, input().split())
        if s * d >= di:
            money += dv
    print(f"Data Set {i}:")
    print(money)
    if i != K + 1:
        print()
