# 뉴비의 기준은 뭘까?
import sys

N, M = map(int, sys.stdin.readline().split())
if M <= 2:
    print("NEWBIE!")
elif N >= M:
    print("OLDBIE!")
else:
    print("TLE!")
