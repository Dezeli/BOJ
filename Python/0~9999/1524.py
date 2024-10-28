# 세준세비
import sys

T = int(sys.stdin.readline().rstrip())
for i in range(T):
    blank = sys.stdin.readline().rstrip()
    N, M = map(int, sys.stdin.readline().split())
    N_list = map(int, sys.stdin.readline().split())
    M_list = map(int, sys.stdin.readline().split())

    if max(N_list) >= max(M_list):
        print("S")
    else:
        print("B")
