# 문자열 폭발
import sys

input = sys.stdin.readline

s = input().rstrip()
b = input().rstrip()
len_b = len(b)

stack = []

for i in s:
    stack.append(i)
    if len(stack) >= len_b:
        if "".join(stack[-len_b:]) == b:
            for i in range(len_b):
                stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")
