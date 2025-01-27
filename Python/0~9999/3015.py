# 오아시스 재결합
import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

N = int(input())

stack = []
cnt = 0

for _ in range(N):
    h = -int(input())
    i = bisect_left(stack, h)
    if i == 0:
        cnt += len(stack) - i
    else:
        cnt += len(stack) - i + 1
    while len(stack) > bisect_right(stack, h):
        stack.pop()
    stack.append(h)

print(cnt)
