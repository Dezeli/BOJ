# 타임 카드
import sys

for _ in range(3):
    timeList = list(map(int, sys.stdin.readline().split(" ")))
    H = timeList[3] - timeList[0] - 1
    M = 60 + timeList[4] - timeList[1] - 1
    S = 60 + timeList[5] - timeList[2]
    if S >= 60:
        S -= 60
        M += 1
    if M >= 60:
        M -= 60
        H += 1
    print(H, M, S)
