# 수 정렬하기

T = int(input())

nums = []
for i in range(T):
    nums.append(int(input()))
nums.sort()
for i in nums:
    print(i)
