# 부호
import sys

for _ in range(3):
    T = int(sys.stdin.readline().rstrip())
    numList = []
    for i in range(T):
        numList.append(int(sys.stdin.readline().rstrip()))
    result = sum(numList)
    if result > 0:
        print("+")
    elif result == 0:
        print(0)
    else:
        print("-")
