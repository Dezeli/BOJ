# 크게 만들기
import sys

input = sys.stdin.readline

N, K = map(int, input().split())

num = input().rstrip()

stack = []

use = 0
for i in num:
    while stack and K:
        if stack[-1] < i and K>use:
            stack.pop()
            use += 1
        else:
            break
    if len(stack)< N-K:
        stack.append(i)

print(''.join(stack))