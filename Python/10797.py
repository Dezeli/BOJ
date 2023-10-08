# 10부제
import sys

num = int(sys.stdin.readline().rstrip())
numList = list(map(int, sys.stdin.readline().split()))
print(numList.count(num))
