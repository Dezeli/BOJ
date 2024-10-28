# 오븐 시계
import sys

H, M = map(int, sys.stdin.readline().split(" "))
P = int(sys.stdin.readline().rstrip())
newH = (H + (M + P) // 60) % 24
newM = (M + P) % 60
print(newH, newM)
