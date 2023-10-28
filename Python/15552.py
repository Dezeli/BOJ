# 빠른 A+B
import sys

T = int(input())
for i in range(T):
    A, B = (sys.stdin.readline().rstrip()).split(" ")
    print(int(A) + int(B))
