# 순서쌍의 곱의 합
import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
mul_nums = sum(nums)

ans = 0
for i in nums:
    mul_nums -= i
    ans += i*mul_nums
print(ans)