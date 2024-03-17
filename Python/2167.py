# 2차원 배열의 합
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

nums = []
for _ in range(N):
    line = list(map(int, input().split()))
    nums.append(line)

K = int(input())
for _ in range(K):
    i, j, x, y = map(int, input().split())

    sum_nums = 0
    for k in range(i-1, x):
        for z in range(j-1, y):
            sum_nums += nums[k][z]
    print(sum_nums)