# 소트인사이드
import sys

N = sys.stdin.readline().rstrip()
nums = ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']

for i in nums:
    print(i*N.count(i), end="")
print()