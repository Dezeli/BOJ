# 최댓값
import copy

numList = []
for i in range(9):
    numList.append(int(input()))
numListCopy = copy.deepcopy(numList)
numList.sort()
print(numList[-1])
print(numListCopy.index(numList[-1]) + 1)
