# TRENER
import sys
from collections import defaultdict

N = int(sys.stdin.readline().rstrip())
playerDict = defaultdict(int)
for _ in range(N):
    playerDict[sys.stdin.readline()[0]] += 1
participateList = []
for key, value in playerDict.items():
    if value >= 5:
        participateList.append(key)
participateList.sort()
for i in participateList:
    print(i, end="")
if len(participateList) == 0:
    print("PREDAJA")