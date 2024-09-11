# 강당 대관
import sys

input = sys.stdin.readline

max_num = 0
for _ in range(7):
    name, num = input().rstrip().split()
    if int(num)>max_num:
        max_num = int(num)
        result = name

print(result)