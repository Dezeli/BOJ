# 주유소
import sys

input = sys.stdin.readline

N = int(input())

roads = list(map(int, input().split()))
oils = list(map(int, input().split()))

o = 1
min_oil = oils[0]

cost = 0

for i in roads:
    cost += min_oil*i
    min_oil = min(min_oil, oils[o])
    o += 1

print(cost)