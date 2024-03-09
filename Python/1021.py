# 회전하는 큐
from collections import deque

N, M = map(int, input().split())

pop_list = list(map(int, input().split()))
nums = deque([i for i in range(1, N+1)])

cnt = 0
for i in pop_list:
    if nums[0]==i:
        nums.popleft()
        continue
    if nums.index(i) < len(nums)/2:
        while nums[0]!=i:
            nums.append(nums.popleft())
            cnt += 1
    else:
        while nums[0]!=i:
            nums.appendleft(nums.pop())
            cnt += 1
    nums.popleft()

print(cnt)