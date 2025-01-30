# 줄 세우기
import sys

input = sys.stdin.readline

line = []

N = int(input())
pick = [0]+ list(map(int, input().split()))

for i in range(1, N+1):
    line.insert(pick[i], i)

print(*line[::-1])