# 단어 공부
import string
import sys

word = sys.stdin.readline().rstrip()
uppercaseList = [i for i in string.ascii_uppercase]
wordAlpList = []
for i in word:
    wordAlpList.append(i.upper())
countList = []
for i in uppercaseList:
    countList.append(wordAlpList.count(i))

result = uppercaseList[countList.index(max(countList))]
countList.sort()
if countList[-1] == countList[-2]:
    print("?")
else:
    print(result)
