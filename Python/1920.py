# 수 찾기
import sys

N = sys.stdin.readline().rstrip()
A = sys.stdin.readline().rstrip().split(" ")
M = sys.stdin.readline().rstrip()
B = sys.stdin.readline().rstrip().split(" ")
A.sort()

def findNum(num, li):
    last = len(li) - 1
    first = 0
    while first <= last:
        avg = (last + first) // 2
        if num < li[avg]:
            last = avg - 1
        elif num > li[avg]:
            first = avg + 1
        else:
            return True
    return False

for i in B:
    if findNum(i, A) == False:
        print(0)
    else:
        print(1)
