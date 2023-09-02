# 임시 반장 정하기
import sys
from collections import defaultdict

S = int(sys.stdin.readline().rstrip())
studentClasses = []
friendDict = defaultdict(list)

for _ in range(S):
    classes = list(map(int, sys.stdin.readline().split()))
    for studentIdx in range(len(studentClasses)):
        for i in range(5):
            if studentClasses[studentIdx][i] == classes[i]:
                friendDict[studentIdx + 1].append(len(studentClasses) + 1)
                friendDict[len(studentClasses) + 1].append(studentIdx + 1)
                break
    studentClasses.append(classes)
maxValue = 0
maxKey = [1]
for key, value in friendDict.items():
    if len(value) > maxValue:
        maxValue = len(value)
        maxKey = [key]
    elif len(value) == maxValue:
        maxKey.append(key)
print(min(maxKey))
