# 스택 2
import sys

input = sys.stdin.readline

N = int(input())

stack = []

for i in range(N):
    ord = list(map(int, input().split()))

    if ord[0] == 1:
        stack.append(ord[1])
    elif ord[0] == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif ord[0] == 3:
        print(len(stack))
    elif ord[0] == 4:
        if stack:
            print(0)
        else:
            print(1)
    elif ord[0] == 5:
        if stack:
            print(stack[-1])
        else:
            print(-1)
