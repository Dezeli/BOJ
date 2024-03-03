# 단지번호붙이기


def numberHomes(home):
    def checkUpDownLeftRight(x, y, num):
        if x <= -1 or x >= len(home[0]) or y <= -1 or y >= len(home):
            return
        if home[y][x] == "1":
            home[y][x] = num
        else:
            return

        checkUpDownLeftRight(x - 1, y, num)
        checkUpDownLeftRight(x + 1, y, num)
        checkUpDownLeftRight(x, y - 1, num)
        checkUpDownLeftRight(x, y + 1, num)

    homeNum = 0
    for rowNum in range(len(home)):
        for oneHomeNum in range(len(home[rowNum])):
            if home[rowNum][oneHomeNum] == "1":
                homeNum += 1
                checkUpDownLeftRight(oneHomeNum, rowNum, homeNum)
    print(homeNum)
    count = []
    for num in range(1, homeNum + 1):
        numCount = 0
        for j in homes:
            numCount += j.count(num)
        count.append(numCount)
    count.sort()
    for i in count:
        print(i)


N = int(input())
homes = []
for i in range(N):
    L = input()
    W = []
    for j in L:
        W.append(j)
    homes.append(W)
numberHomes(homes)
