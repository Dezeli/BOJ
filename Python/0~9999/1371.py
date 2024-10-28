# 가장 많은 글자
import sys
from string import ascii_lowercase

text = sys.stdin.read()
alphabets = list(ascii_lowercase)
countList = []
for alp in alphabets:
    countList.append(text.count(alp))
maxCnt = max(countList)
for idx, cnt in enumerate(countList):
    if cnt == maxCnt:
        print(alphabets[idx], end="")
print()
