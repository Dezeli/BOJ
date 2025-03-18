# 오등큰수
import sys
from collections import defaultdict

input = sys.stdin.readline

cnt = defaultdict(int)

N = int(input())
nums = list(map(int, input().split()))

for i in nums:
    cnt[i] += 1

stack = []

ans = []
while nums:
    n = nums.pop()
    while stack:
        l = stack.pop()
        if cnt[n] < cnt[l]:
            stack.append(l)
            break
    if stack:
        ans.append(stack[-1])
    else:
        ans.append(-1)
    stack.append(n)

print(*ans[::-1])
