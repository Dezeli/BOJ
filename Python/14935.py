# FA
import sys

num = int(sys.stdin.readline().rstrip())
numList = [num]


def F(x):
    fNum = int(str(x)[0]) * len(str(x))
    if fNum == numList[-1]:
        return print("FA")
    elif fNum in numList:
        return print("NFA")
    else:
        numList.append(fNum)
        F(fNum)


F(num)
