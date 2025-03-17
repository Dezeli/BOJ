# 택배
import sys

input = sys.stdin.readline

N, C = map(int, input().split())
M = int(input())

send = []
for _ in range(M):
    a, b, c = map(int, input().split())
    