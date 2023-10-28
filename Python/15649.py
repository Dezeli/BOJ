# N과 M(1)
import sys

N, M = map(int, sys.stdin.readline().split())


def sunyeol(numList):
    def addSunyeol(popList, testList):
        for i in range(len(testList)):
            sunList = list(popList)
            addList = list(testList)
            if len(popList) != M:
                sunList.append(addList.pop(i))
                addSunyeol(sunList, addList)

        if len(popList) == M:
            for i in popList:
                print(i, end=" ")
            print()

    for i in range(len(numList)):
        addList = list(numList)
        popList = [addList.pop(i)]
        addSunyeol(popList, addList)


sunyeol([i for i in range(1, N + 1)])
