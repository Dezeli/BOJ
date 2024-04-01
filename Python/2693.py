# N번째 큰 수
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    nums = list(map(int, input().split()))
    nums.sort()
    print(nums[-3])