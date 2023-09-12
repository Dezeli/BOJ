# 논리학 교수
import sys

num_dict = {}
for i in range(51):
    num_dict[i] = 0

N = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().split()))

for i in nums:
    num_dict[i] += 1

check = False
for i in range(51):
    if num_dict[50 - i] == 50 - i:
        print(50 - i)
        check = True
        break
if not check:
    print(-1)
