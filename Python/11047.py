# 동전 0
import sys

N, K = map(int, sys.stdin.readline().split(" "))
coins = []

for _ in range(N):
    coin = int(sys.stdin.readline().rstrip())
    if coin <= K:
        coins.append(coin)
coins.reverse()

min_need = sys.maxsize

for i in range(len(coins)):
    need = 0
    money = K
    for coin in coins[i:]:
        n, money = divmod(money, coin)
        need += n
        if money == 0 or need > min_need:
            break
    min_need = min([min_need, need])

print(min_need)
