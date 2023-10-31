# 달달함이 넘쳐흘러
import sys

a1, a2, a3 = map(int, sys.stdin.readline().split(" "))
c1, c2, c3 = map(int, sys.stdin.readline().split(" "))
print(c1 - a3, c2 // a2, c3 - a1)
