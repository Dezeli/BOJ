# 1로 만들기
import sys

num = int(sys.stdin.readline())
cntList = [0, 0]

for i in range(2, num + 1):
    if i % 3 == 0 and i % 2 == 0:
        cntList.append(min(cntList[i // 3], cntList[i // 2], cntList[i - 1]) + 1)

    elif i % 3 == 0:
        cntList.append(min(cntList[i // 3], cntList[i - 1]) + 1)
    elif i % 2 == 0:
        cntList.append(min(cntList[i // 2], cntList[i - 1]) + 1)
    else:
        cntList.append(cntList[i - 1] + 1)

print(cntList[-1])
