# 인사성 밝은 곰곰이
import sys

input = sys.stdin.readline

N = int(input())

cnt = 0
hi = set()
for _ in range(N):
    name = input().rstrip()
    if name=="ENTER":
        cnt += len(hi)
        hi = set()
        continue
    else:
        hi.add(name)
cnt += len(hi)

print(cnt)