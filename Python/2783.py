# 삼각 김밥

X, Y = map(int, input().split())

N = int(input())

min_price = X/Y

for _ in range(N):
    X, Y = map(int, input().split())

    min_price = min(min_price, X/Y)

print(min_price*1000)