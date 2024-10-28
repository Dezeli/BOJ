# Koszykarz
# 폴란드어 문제
import sys

K, W, M = map(int, sys.stdin.readline().split())
if (W - K) % M == 0:
    print((W - K) // M)
else:
    print((W - K) // M + 1)
