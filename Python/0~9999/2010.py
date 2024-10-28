# 플러그
import sys

input = sys.stdin.readline

N = int(input())

plug = 1

for _ in range(N):
    plug += int(input()) - 1

print(plug)
