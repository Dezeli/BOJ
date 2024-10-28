# 심부름 가는길
import sys

secondList = []
for _ in range(4):
    secondList.append(int(sys.stdin.readline()))
print(sum(secondList) // 60)
print(sum(secondList) % 60)
