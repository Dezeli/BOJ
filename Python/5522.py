# 카드 게임
import sys

cardList = []
for _ in range(5):
    cardList.append(int(sys.stdin.readline()))
print(sum(cardList))
