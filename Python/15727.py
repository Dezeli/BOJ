# 조별과제를 하려는데 조장이 사라졌다
import sys

N = int(sys.stdin.readline().rstrip())
if N % 5 == 0:
    print(N // 5)
else:
    print(N // 5 + 1)
