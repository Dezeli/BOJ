# ABC 

nums = list(map(int, input().split()))
nums.sort()

s = input()

new = []

for i in s:
    if i=='A':
        new.append(nums[0])
    if i=='B':
        new.append(nums[1])
    if i=='C':
        new.append(nums[2])

print(*new)
    