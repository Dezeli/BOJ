# 통계학
import sys

N = int(sys.stdin.readline().rstrip())
numList = []
numDict = {}
for i in range(N):
    num = int(sys.stdin.readline().rstrip())
    numList.append(num)
    numDict[num] = numDict.setdefault(num, 0) + 1
numList.sort()
sortDict = sorted(numDict.items(), key=lambda x: x[1], reverse=True)
most = sortDict[0][1]
mostList = []
for i in range(len(sortDict)):
    if sortDict[i][1] == most:
        mostList.append(sortDict[i][0])
    else:
        break
mostList.sort()

print(round(sum(numList) / N))
print(numList[N // 2])
try:
    print(mostList[1])
except:
    print(mostList[0])
print(max(numList) - min(numList))
