# 한조서열정리하고옴ㅋㅋ
import sys

input = sys.stdin.readline

N = int(input())
mount = list(map(int, input().split()))

max_kill = 0

last = 0
cnt = 0
for i in mount:
    if last < i:
        last = i
        max_kill = max(max_kill, cnt)
        cnt = 0
    else:
        cnt += 1
max_kill = max(max_kill, cnt)

print(max_kill)
