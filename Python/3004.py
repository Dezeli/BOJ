# CRNE
import sys

N = int(sys.stdin.readline().rstrip())
print((N // 2 + 1) * (N // 2 + N % 2 + 1))
