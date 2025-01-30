# 막대기
import sys

input = sys.stdin.readline

N = int(input())

polls = [int(input()) for _ in range(N)]

cnt = 1
p1 = polls.pop()

while polls:
    p2 = polls.pop()
    if p2 > p1:
        cnt += 1
        p1 = p2

print(cnt)
