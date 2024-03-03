# EKO
import sys

N, M = map(int, (sys.stdin.readline().rstrip()).split(" "))
treeList = list(map(int, (sys.stdin.readline().rstrip()).split(" ")))
treeList.append(0)
treeList.sort(reverse=True)
treeLength = 0
lastTree = 0
trees = 0
for i in range(len(treeList) - 1):
    treeLength += (treeList[i] - treeList[i + 1]) * (i + 1)
    if treeLength >= M:
        lastTree = treeList[i + 1]
        trees = i + 1
        break

lastTree += (treeLength - M) // trees
print(lastTree)
