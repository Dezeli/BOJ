# Bałwanek
# 폴란드어 문제
import sys

X, K = map(int, sys.stdin.readline().split())
if 7 * K <= X:
    print(7 * K * 1000)
elif 7 * K / 2 <= X:
    print(7 * K * 500)
elif 7 * K / 4 <= X:
    print(7 * K * 250)
else:
    print(0)
