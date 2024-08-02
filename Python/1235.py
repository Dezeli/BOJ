# 학생 번호
import sys

input = sys.stdin.readline

N = int(input())

nums = []
for _ in range(N):
    nums.append(str(input().rstrip()))
for i in range(1, len(nums[0])+1):
    results=[]
    for j in range(N):
        if nums[j][-i:] in results:
            break
        else:
            results.append(nums[j][-i:])
    if len(results)==N:
        print(i)
        break