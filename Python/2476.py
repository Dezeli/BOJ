# 주사위 게임

N = int(input())

max_price = 0
for _ in range(N):
    a, b, c = map(int, input().split())
    if a == b == c:
        max_price = max(max_price, 10000 + a * 1000)
    elif a == b:
        max_price = max(max_price, 1000 + a * 100)
    elif b == c:
        max_price = max(max_price, 1000 + b * 100)
    elif c == a:
        max_price = max(max_price, 1000 + c * 100)
    else:
        max_price = max(max_price, max([a, b, c]) * 100)

print(max_price)
