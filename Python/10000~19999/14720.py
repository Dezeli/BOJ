# 우유 축제
import sys

input = sys.stdin.readline

N = int(input())

shop = list(map(int, input().split()))

now = 0

for i in shop:
    if i == now % 3:
        now += 1

print(now)
