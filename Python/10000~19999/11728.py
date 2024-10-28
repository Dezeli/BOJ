# 배열 합치기
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
A += list(map(int, input().split()))

A.sort()
print(*A)
