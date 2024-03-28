# 진법 변환

nums = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N, B = input().split()
ans = 0
for i, num in enumerate(N[::-1]):
    ans += int(B)**i*nums.index(num)
print(ans)