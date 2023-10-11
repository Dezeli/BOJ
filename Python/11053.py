# 가장 긴 증가하는 부분 수열

N = int(input())

suyeolList = list(map(int, input().split()))
numList = []
numList.append(1)
for i in range(1, len(suyeolList)):
    maxList = [1]
    for j in range(i):
        if suyeolList[j] < suyeolList[i]:
            maxList.append(numList[j])
    if maxList != [1]:
        numList.append(max(maxList) + 1)
    else:
        numList.append(1)
print(max(numList))
