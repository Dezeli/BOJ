# 히스토그램에서 가장 큰 직사각형
import sys

input = sys.stdin.readline

while True:
    hist = list(map(int, input().split()))
    n = hist[0]
    if n == 0:
        break
    hist = hist[1:]

    stack = []
    ans = 0
    for i in range(n):
        idx = i
        while stack and stack[-1][1] > hist[i]:
            idx, height = stack.pop()
            rst = (i - idx) * height
            ans = max(ans, rst)

        stack.append([idx, hist[i]])

    while stack:
        idx, height = stack.pop()
        rst = (n - idx) * height
        ans = max(ans, rst)

    print(ans)
