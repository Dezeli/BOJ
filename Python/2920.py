# NOTE 

nums = list(map(int, input().split(" ")))

lenNums = len(nums)
for i in range(len(nums) - 1):
    if nums[i] > nums[i + 1]:
        lenNums += 1
    else:
        lenNums -= 1
if lenNums == 1:
    print("ascending")
elif lenNums == len(nums) * 2 - 1:
    print("descending")
else:
    print("mixed")
