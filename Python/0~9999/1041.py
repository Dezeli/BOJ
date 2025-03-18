# 주사위
import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
three = [
    [0, 1, 2],
    [0, 1, 3],
    [0, 2, 4],
    [0, 3, 4],
    [5, 1, 2],
    [5, 1, 3],
    [5, 2, 4],
    [5, 3, 4],
]
min_three = 151
for a, b, c in three:
    min_three = min(sum([nums[a], nums[b], nums[c]]), min_three)

two = [
    [0, 1],
    [0, 2],
    [0, 3],
    [0, 4],
    [1, 2],
    [1, 3],
    [1, 5],
    [2, 4],
    [2, 5],
    [3, 4],
    [3, 5],
    [4, 5],
]
min_two = 101
for a, b in two:
    min_two = min(sum([nums[a], nums[b]]), min_two)


cnt = 0
cnt += min_three * 4
cnt += min_two * 4 * (2 * N - 3)
cnt += min(nums) * (N - 2) * (N - 1) * 4 + min(nums) * (N - 2) * (N - 2)

if N == 1:
    print(sum(nums) - max(nums))
else:
    print(cnt)
