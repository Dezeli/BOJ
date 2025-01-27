# 낚이고 낚아라
import sys

input = sys.stdin.readline

N, K = map(int, input().split())

fish = []
for _ in range(N):
    P = int(input())
    dots = list(map(int, input().split()))
    max_dot = 0
    for i in range(0, P * 2, 2):
        x, y = dots[i], dots[i + 1]
        max_dot = max(x**2 + y**2, max_dot)
    fish.append(max_dot)

fish.sort()
print(f"{fish[K-1]}" + ".00")
