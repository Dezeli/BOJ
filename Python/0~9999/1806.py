# 부분합
import sys

input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))

left, right = 0, 0
sum_num = 0
min_len = sys.maxsize

while True:
    if sum_num >= S:
        min_len = min(min_len, right - left)
        sum_num -= nums[left]
        left += 1
    elif right == N:
        break
    else:
        sum_num += nums[right]
        right += 1

if min_len == sys.maxsize:
    print(0)
else:
    print(min_len)
