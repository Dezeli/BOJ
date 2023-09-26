# 나무꾼 이다솜
import sys

N, C, W = map(int, sys.stdin.readline().split())

woods = []
for _ in range(N):
    woods.append(int(sys.stdin.readline().rstrip()))

woods.sort()

max_money = 0
for i in range(1, woods[-1] + 1):
    money = 0
    L = i
    for j in woods:
        K = j // i
        if j % i == 0:
            cut_money = K * L * W - C * (K - 1)
            if cut_money > 0:
                money += cut_money
        else:
            cut_money = K * L * W - C * K
            if cut_money > 0:
                money += cut_money
    max_money = max(max_money, money)
print(max_money)
