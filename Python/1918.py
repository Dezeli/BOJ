# 후위 표기식
import sys
from collections import deque

input = sys.stdin.readline

S = input().rstrip()

stack = deque([])
for i in S:
    if i==')':
        bracket1 = deque([])
        bracket2 = deque([])
        bracket3 = deque([])
        while True:
            j = stack.pop()
            if j =='(':
                break
            bracket1.appendleft(j)
        
        check = ''
        while bracket1:
            j = bracket1.popleft()
            if check:
                bracket2.append(j)
                bracket2.append(check)
                check = ''
                continue
            if j=="*" or j=="/":
                check = j
            else:
                bracket2.append(j)

        check = ''
        while bracket2:
            j = bracket2.popleft()
            if j == "+" or j=="-":
                bracket3.append(check)
                check = j
            else:
                bracket3.append(j)
        bracket3.append(check)
        stack.append(''.join(bracket3))
    else:
        stack.append(i)

stack2 = deque([])
stack3 = deque([])
check = ''
while stack:
    j = stack.popleft()
    if check:
        stack2.append(j)
        stack2.append(check)
        check = ''
        continue
    if j=="*" or j=="/":
        check = j
    else:
        stack2.append(j)

check = ''
while stack2:
    j = stack2.popleft()
    if j == "+" or j=="-":
        stack3.append(check)
        check = j
    else:
        stack3.append(j)
stack3.append(check)
print(''.join(stack3))