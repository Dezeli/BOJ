# 도둑
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M, K = map(int, input().split())
    house = list(map(int, input().split()))

    p_money = [0]

    sum_m = 0
    for _ in range(2):
        for i in house:
            sum_m += i
            p_money.append(sum_m)

    steal = 0
    for i in range(M, M + N):
        if p_money[i] - p_money[i - M] < K:
            steal += 1
    if M == N and steal > 0:
        steal = 1
    print(steal)
