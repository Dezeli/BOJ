# 히스토그램
import sys

input = sys.stdin.readline

N = int(input())
hist = [int(input()) for _ in range(N)]

stack = []
ans = 0
for i in range(N):
    idx = i
    while (stack and stack[-1][1] > hist[i]):
        idx, height = stack.pop()
        rst = (i - idx) * height
        ans = max(ans, rst)

    stack.append([idx, hist[i]])
    
while stack:
    idx, height = stack.pop()
    rst = (N - idx) * height
    ans = max(ans, rst)

print(ans)