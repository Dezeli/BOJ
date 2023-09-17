# 주사위 세개
import sys

dice = list(map(int, sys.stdin.readline().split(" ")))
money = 0
for i in range(1, 7):
    if dice.count(i) == 2:
        money = 1000 + 100 * i
        break
    elif dice.count(i) == 3:
        money = 10000 + 1000 * i
        break
if money == 0:
    money = max(dice) * 100
print(money)
