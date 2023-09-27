# 탑
import sys

N = sys.stdin.readline()

towerList = list(map(int, sys.stdin.readline().split()))
towerDict = {}
towerCheck = list(towerList)
stack = []
while towerCheck:
    towerNum = len(towerCheck)
    tower = towerCheck.pop()
    while stack:
        if stack[-1] < tower:
            towerDict[stack[-1]] = towerNum
            stack.pop()
        else:
            break
    stack.append(tower)
for i in stack:
    towerDict[i] = 0
for i in towerList:
    print(towerDict[i], end=" ")
