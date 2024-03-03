# 선물

N, X = map(int, input().split())
prices = list(map(int, input().split()))

min_price = 2000

for i in range(N - 1):
    min_price = min(min_price, prices[i] + prices[i + 1])

print(min_price * X)
