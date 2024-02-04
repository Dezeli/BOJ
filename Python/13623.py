# Zero or One

nums = list(map(int, input().split()))

if sum(nums)==0 or sum(nums)==3:
    print("*")
if sum(nums)==1:
    for i in range(len(nums)):
        if nums[i]==1:
            if i==0:
                print("A")
            elif i==1:
                print("B")
            else:
                print("C")
if sum(nums)==2:
    for i in range(len(nums)):
        if nums[i]==0:
            if i==0:
                print("A")
            elif i==1:
                print("B")
            else:
                print("C")

            
