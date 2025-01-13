# 괄호의 값
import sys

input = sys.stdin.readline

S = input().rstrip()

correct = True
stack = []
cnt = 0
for i in S:
    if i=='(' or i=='[':
        stack.append(i)
        cnt += 1
    else:
        stack.append(i)
        cnt -= 1
        if cnt==0:
            close = []
            while stack:
                last = stack.pop()
                if last==')' and last==']':
                    close.append(last)
                else:
                    c = close.pop()
                    if last=='(' and c==')':
                        pass
                    elif last=='[' and c==']':
                        pass
                    else:
                        correct = False
                        break
    if not correct:
        break

