# 평균

N = int(input())
scoreList = input().split(" ")
for i in range(len(scoreList)):
    scoreList[i] = int(scoreList[i])
scoreList.sort()
for i in range(len(scoreList)):
    scoreList[i] = int(scoreList[i]) / int(scoreList[-1]) * 100
scoreSum = 0
for i in scoreList:
    scoreSum += float(i)
print(scoreSum / N)
