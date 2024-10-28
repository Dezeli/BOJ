# 꿀 아르바이트
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
pay = list(map(int, input().split()))

cur_sum = 0
l = 0
r = m - 1
for i in range(r + 1):
    cur_sum += pay[i]
max_sum = cur_sum

while r < n - 1:
    cur_sum -= pay[l]
    l += 1
    r += 1
    cur_sum += pay[r]

    max_sum = max(max_sum, cur_sum)
print(max_sum)
