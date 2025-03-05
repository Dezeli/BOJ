# 주식
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    days = list(map(int, input().split()))
    max_price = 0
    answer = 0
    for i in range(N-1, -1, -1):
        if max_price < days[i]:
            max_price = days[i]
        elif max_price > days[i]:
            answer += (max_price - days[i])
    print(answer)