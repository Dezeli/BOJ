# 너의 핸들은
import sys

input = sys.stdin.readline

N, I = map(int, input().split())

names = [input() for _ in range(N)]
names.sort()
print(names[I-1])