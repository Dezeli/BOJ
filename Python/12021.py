# 보물 찾기
import sys

input = sys.stdin.readline

a, b = map(int, input().split())


while True:
    newa = (a + b) / 2
    newb = 2 * (a * b) / (a + b)

    if newa == a and newb == b:
        print(a, b)
        break

    a = newa
    b = newb
