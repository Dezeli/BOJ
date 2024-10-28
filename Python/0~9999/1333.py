# 부재중 전화
import sys


def noticeCall():
    N, L, D = map(int, sys.stdin.readline().split(" "))
    breakStart = -5
    for _ in range(N):
        breakStart += L + 5
        breakFinish = breakStart + 5
        for i in range(breakStart, breakFinish):
            if i % D == 0:
                print(i)
                return
    while True:
        if breakFinish % D == 0:
            print(breakFinish)
            return
        breakFinish += 1


noticeCall()
