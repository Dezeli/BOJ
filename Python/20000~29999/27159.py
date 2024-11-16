# 노 땡스!
import sys

input = sys.stdin.readline

N = int(input())
x = list(map(int, input().split()))

score = 0
last = 0
for i in x:
    if i == last + 1:
        last = i
        continue
    score += i
    last = i

print(score)
