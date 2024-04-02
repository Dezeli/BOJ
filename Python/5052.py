# 전화번호 목록
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    phone_nums = []
    for _ in range(n):
        num = input().rstrip()
        phone_nums.append(num)
    phone_nums.sort()
    ans = True
    for i in range(n-1):
        if phone_nums[i] == phone_nums[i+1][:len(phone_nums[i])]:
            ans = False
            break
    
    if ans:
        print("YES")
    else:
        print("NO")