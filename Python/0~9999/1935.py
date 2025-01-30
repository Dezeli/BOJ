# 후위 표기식2
import sys

input = sys.stdin.readline

N = int(input())

S = input().rstrip()
nums = []
for i in range(N):
    nums.append(int(input()))
stack = []
for i in S:
    if i == "+":
        a = stack.pop()
        b = stack.pop()
        stack.append(a + b)
    elif i == "-":
        a = stack.pop()
        b = stack.pop()
        stack.append(b - a)
    elif i == "/":
        a = stack.pop()
        b = stack.pop()
        stack.append(b / a)
    elif i == "*":
        a = stack.pop()
        b = stack.pop()
        stack.append(a * b)
    else:
        if i.isupper():
            stack.append(nums[ord(i) - ord("A")])

for j in stack:
    print("{:.2f}".format(j))
