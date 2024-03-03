# 유진수
import sys


def checkUjin():
    N = sys.stdin.readline().rstrip()
    for i in range(1, len(N)):
        front = 1
        back = 1
        for j in range(0, i):
            front *= int(N[j])
        for j in range(i, len(N)):
            back *= int(N[j])
        if front == back:
            return "YES"
    return "NO"


result = checkUjin()
print(result)
