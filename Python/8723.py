# Patyki
# 폴란드어 문제
import sys

poll = list(map(int, sys.stdin.readline().split()))
poll.sort()
if poll[0] == poll[1] == poll[2]:
    print(2)
elif poll[2] ** 2 == poll[0] ** 2 + poll[1] ** 2:
    print(1)
else:
    print(0)
