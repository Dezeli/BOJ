# 인공지능 시계
import sys

H, M, S = map(int, sys.stdin.readline().split(" "))
P = int(sys.stdin.readline().rstrip())
newS = (S + P) % 60
newM = ((S + P) // 60 + M) % 60
newH = (((S + P) // 60 + M) // 60 + H) % 24
print(newH, newM, newS)
