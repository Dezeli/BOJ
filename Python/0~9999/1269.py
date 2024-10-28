# 대칭 차집합
import sys

input = sys.stdin.readline

nA, nB = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
print(len(A - B) + len(B - A))
