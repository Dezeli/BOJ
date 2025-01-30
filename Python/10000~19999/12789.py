# 도키도키 간식드리미
import sys

input = sys.stdin.readline

N = int(input())
line = list(map(int, input().split()))

stack = [N + 1]

num = 1
snack = True
for i in line:
    while stack:
        n = stack.pop()
        if n == num:
            num += 1
        else:
            stack.append(n)
            break

    if i == num:
        num += 1
        continue

    if stack[-1] > i:
        stack.append(i)
    else:
        snack = False
        break

if snack:
    print("Nice")
else:
    print("Sad")
