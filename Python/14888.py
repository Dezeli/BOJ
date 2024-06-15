# 연산자 끼워넣기
import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
op = list(map(int, input().split()))

maximum = -1e9
minimum = 1e9


def dfs(d, total, plus, minus, multiply, divide):
    global maximum, minimum
    if d == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        dfs(d + 1, total + A[d], plus - 1, minus, multiply, divide)
    if minus:
        dfs(d + 1, total - A[d], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(d + 1, total * A[d], plus, minus, multiply - 1, divide)
    if divide:
        dfs(d + 1, int(total / A[d]), plus, minus, multiply, divide - 1)


dfs(1, A[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)
