# 좋은 단어
import sys

input = sys.stdin.readline

N = int(input())
cnt = 0

for _ in range(N):
    stack = []
    s = input().rstrip()
    for i in s:
        if stack:
            if stack[-1]==i:
                stack.pop()
                continue
        stack.append(i)

    if not stack:
        cnt += 1

print(cnt)