# 스택
import sys

N = int(sys.stdin.readline())
stack = []
for i in range(N):
    com = sys.stdin.readline()
    if com[:3] == "pus":
        stack.append(int(com[5:]))
    elif com[:3] == "top":
        if len(stack) == 0:
            print("-1")
        else:
            print(stack[-1])
    elif com[:3] == "siz":
        print(len(stack))
    elif com[:3] == "emp":
        if len(stack) == 0:
            print("1")
        else:
            print("0")
    else:
        if len(stack) == 0:
            print("-1")
        else:
            print(stack[-1])
            stack.pop(-1)
