# Haughty Cuisine
import sys

input = sys.stdin.readline

m = int(input())
for _ in range(m):
    menu = list(input().rstrip().split())

for i in menu:
    print(i)
