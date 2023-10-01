# MODULO 

nums = []
restList = []
for i in range(10):
    nums.append(int(input()))
for i in nums:
    restList.append(i % 42)
restList = set(restList)
print(len(restList))
