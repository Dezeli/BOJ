# 이 대회는 이제 제 겁니다
import sys

input = sys.stdin.readline

A, P, C = map(int, input().split())
print(max(A + C, P))
