# 괄호의 값
import sys

input = sys.stdin.readline

S = input().rstrip()

correct = True
stack = []

for i in S:
    if i == "(" or i == "[":
        stack.append(i)
    else:
        cnt = 0
        if stack:
            last = stack.pop()
        else:
            correct = False
            break
        while True:
            if type(last) == int:
                cnt += last
                if stack:
                    last = stack.pop()
                else:
                    correct = False
                    break
            else:
                cnt = max(1, cnt)
                if last == "(" and i == ")":
                    stack.append(cnt * 2)
                elif last == "[" and i == "]":
                    stack.append(cnt * 3)
                else:
                    correct = False
                break

    if not correct:
        break


for i in stack:
    if type(i) == str:
        correct = False
        break

if correct:
    print(sum(stack))
else:
    print(0)
