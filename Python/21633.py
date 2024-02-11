# Bank Transfer

k = int(input())
money = k/100+25
if money>2000: money = 2000
if money<100: money = 100
print("{:.2f}".format(money))