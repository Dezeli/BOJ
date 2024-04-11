# 포도주 시식
import sys

input = sys.stdin.readline

n = int(input())
grapes = [int(input()) for _ in range(n)]

if n<=2:
    print(sum(grapes))
else:
    max_drink = [0 for _ in range(n)]

    max_drink[0] = grapes[0]
    max_drink[1] = grapes[0] + grapes[1]
    max_drink[2] = max(grapes[0]+grapes[2], grapes[1]+grapes[2], max_drink[1])

    for i in range(3, n):
        max_drink[i] = max(grapes[i] + max_drink[i-2], grapes[i] + grapes[i-1] + max_drink[i-3], max_drink[i-1])

    print(max(max_drink))