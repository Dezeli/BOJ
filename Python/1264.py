# Vowels
import sys
from collections import defaultdict

checkList = ["A", "E", "O", "U", "I", "a", "e", "o", "u", "i"]
T = sys.stdin.readline().rstrip()
while T != "#":
    alpDict = defaultdict(int)
    for i in T:
        if i in checkList:
            alpDict[i] += 1
    dictValueSum = [i for i in alpDict.values()]
    print(sum(dictValueSum))
    T = sys.stdin.readline().rstrip()
    