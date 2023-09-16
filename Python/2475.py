# 검증수
import sys

nums = list(map(int, sys.stdin.readline().split(" ")))
sumList = []
for i in nums:
    sumList.append(i**2)
print(sum(sumList) % 10)
