# 싱크홀
import sys

input = sys.stdin.readline

V, W, D = map(int, input().split())

cnt = -1
while D > 0:
    D -= 5 * (W / V) ** 2
    V = V * 8 / 10
    cnt += 1

print(cnt)
