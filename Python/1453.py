# 피시방 알바

import sys

N = int(sys.stdin.readline().rstrip())
customers = list(set(list(map(int, sys.stdin.readline().split()))))
print(N - len(customers))
