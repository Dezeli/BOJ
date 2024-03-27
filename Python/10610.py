# 30

N = input()
nums = []
for i in N:
    nums.append(int(i))
nums.sort(reverse=True)

if '0' in N and sum(nums)%3==0:
    print(''.join(map(str, nums)))
else:
    print(-1)