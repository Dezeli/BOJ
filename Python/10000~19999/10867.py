# 중복 빼고 정렬하기
import sys

input = sys.stdin.readline

N = int(input())
nums = list(set(map(int, input().split())))
nums.sort()
print(*nums)
